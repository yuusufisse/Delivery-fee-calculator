# delivery-fee-calculator

### Specification
Rules for calculating a delivery fee
* If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€. For example if the cart value is 8.90€, the surcharge will be 1.10€.
* A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
  * Example 1: If the delivery distance is 1499 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
  * Example 2: If the delivery distance is 1500 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
  * Example 3: If the delivery distance is 1501 meters, the delivery fee is: 2€ base fee + 1€ for the first 500 m + 1€ for the second 500 m => 4€
* If the number of items is five or more, an additional 50 cent surcharge is added for each item above and including the fifth item. An extra "bulk" fee applies for more than 12 items of 1,20€
  * Example 1: If the number of items is 4, no extra surcharge
  * Example 2: If the number of items is 5, 50 cents surcharge is added
  * Example 3: If the number of items is 10, 3€ surcharge (6 x 50 cents) is added
  * Example 4: If the number of items is 13, 5,70€ surcharge is added ((9 * 50 cents) + 1,20€)
* The delivery fee can __never__ be more than 15€, including possible surcharges.
* The delivery is free (0€) when the cart value is equal or more than 100€. 
* During the Friday rush (3 - 7 PM UTC), the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x. However, the fee still cannot be more than the max (15€).

## Backend specifics

### Task
Build an HTTP API which could be used for calculating the delivery fee. This task was imlemented in Python.

### Specification
Implement an HTTP API (single endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

#### Request
Example: 
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2023-02-03T13:00:00Z"}
```

##### Field details

| Field             | Type  | Description                                                           | Example value                             |
|:---               |:---   |:---                                                                   |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                               |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.  |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.               |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in [ISO format](https://en.wikipedia.org/wiki/ISO_8601).    |__2023-02-03T13:00:00Z__                   |

#### Response
Example:
```json
{"delivery_fee": 710}
```

#### Testing
##### Using Postman to test:

Example 1:
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 5, "time": "2023-02-03T13:00:00Z"}
```

Response:
```json
{"delivery_fee": 760}
```

Example 2:
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2023-02-03T16:00:00Z"}
```

Response
```json
{"delivery_fee": 852}
```
##### Usung the test_fee file
<p align="center" border="none">
  <img alt="test image" src="Delivery-fee-calculator\test.png" align="center">
</p>
