from flask import Flask, request, jsonify
import datetime
import math

class Cart():
    def __init__(self):
        self.cart_value = request.json["cart_value"]
        self.delivery_distance = request.json["delivery_distance"]
        self.number_of_items = request.json["number_of_items"]
        self.time = datetime.datetime.strptime(request.json["time"],"%Y-%m-%dT%H:%M:%S%z")
        self.delivery_fee = 0

    def small_price_fee(self):
        '''
        If the cart value is less than 10€, a small order surcharge is added to the delivery price.
        '''
        if self.cart_value < 1000:
            self.delivery_fee = 1000 - self.cart_value

    def check_fee_threshold(self):
        '''
        The delivery fee can never be more than 15€, including possible surcharges.
        '''
        self.delivery_fee = min(self.delivery_fee, 1500)

    def rush_charge(self):
        ''''
        During the Friday rush (3 - 7 PM UTC), the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x. However, the fee still cannot be more than the max (15€).
        '''
        if 15 <= self.time.hour <= 19:
            self.delivery_fee *= 1.2
            self.delivery_fee = min(self.delivery_fee, 1500)

    def delivery_fee_calculator(self):
        '''
        A delivery fee for the distance
        '''
        if self.delivery_distance <= 1000:
            self.delivery_fee += 200
        else:
            self.delivery_fee += 200 + (math.ceil(self.delivery_distance  / 500) - 2) * 100 

    def quantity_fee(self):
        '''
        If the number of items is five or more, an additional 50 cent surcharge is added for each item above four
        '''
        if self.number_of_items >= 5:
            item_surcharge = (self.number_of_items - 4) * 50
            bulk_fee = 120 if self.number_of_items > 12 else 0
            self.delivery_fee += item_surcharge + bulk_fee

app = Flask(__name__)

@app.route("/delivery_fee", methods=["POST"])
def delivery_fee():
    cart = Cart()
    cart.small_price_fee()
    cart.delivery_fee_calculator()
    cart.quantity_fee()
    cart.check_fee_threshold()
    cart.rush_charge()
    return jsonify({"delivery_fee": int(cart.delivery_fee)})

if __name__ == '__main__':
    app.run(debug=True)
