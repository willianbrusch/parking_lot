# PARKING LOT API

Use this URL as base to requests:

> `http://127.0.0.1:8000/`

## Endpoints:

### POST api/accounts/

- don't need authentication

> #### request body:
>
>```
> {
> 	"username": "admin",
> 	"password": "1234",
> 	"is_superuser": true,
> 	"is_staff": true
> }
> ```
-  **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "id": 1,
>   "is_superuser": true,
>   "is_staff": true,
>   "username": "admin"
> }
>```

### POST api/login/

- don't need authentication

> #### request body:
>
>```
> {
> 	"username": "admin",
> 	"password": "1234"
> }
> ```
-  **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
> }
>```

### POST api/levels/

- Header -> Authorization: Token-admin

> #### request body:
>
>```
> {
> 	"name": "floor 1",
> 	"fill_priority": 2,
> 	"bike_spots": 1,
> 	"car_spots": 2
> }
> ```
-  **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "id": 1,
>   "name": "floor 1",
>   "fill_priority": 2,
>   "available_spots": {
>     "available_bike_spots": 1,
>     "available_car_spots": 2
>   }
> }
>```

### GET api/levels/

-  **If everything goes right:** http status code: 200
> #### response body:
>
>```
> [
>   {
>     "id": 1,
>     "name": "floor 1",
>     "fill_priority": 5,
>     "available_spots": {
>       "available_bike_spots": 20,
>       "available_car_spots": 50
>     }
>   },
>   {
>     "id": 2,
>     "name": "floor 2",
>     "fill_priority": 3,
>     "available_spots": {
>       "available_bike_spots": 10,
>       "available_car_spots": 30
>     }
>   }
> ]
>```

### POST api/pricings/

- Header -> Authorization: Token-admin

> #### request body:
>
>```
> {
> 	"a_coefficient": 100,
> 	"b_coefficient": 100
> }
> ```
-  **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "id": 1,
>   "a_coefficient": 100,
>   "b_coefficient": 100
> }
>```

### POST api/vehicles/

- Header -> Authorization: Token-admin

> #### request body:
>
>```
> {
> 	"vehicle_type": "car",
> 	"license_plate": "AYO1029"
> }
> ```
-  **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "id": 1,
>   "license_plate": "AYO1029",
>   "vehicle_type": "car",
>   "arrived_at": "2021-01-25T17:16:25.727541Z",
>   "paid_at": null,
>   "amount_paid": null,
>   "spot": {
>     "id": 2,
>     "variety": "car",
>     "level_name": "floor 1"
>   }
> }
>```

### POST api/vehicles/<int:vehicle_id>/

- Header -> Authorization: Token-admin


-  **If everything goes right:** http status code: 200
> #### response body:
>
>```
> {
>   "license_plate": "AYO1029",
>   "vehicle_type": "car",
>   "arrived_at": "2021-01-21T19:36:55.364610Z",
>   "paid_at": "2021-01-21T19:37:23.016452Z",
>   "amount_paid": 100,
>   "spot": null
> }
>```

