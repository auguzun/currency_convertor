# currency_convertor

 Simple currency converter
 

Example of request to convert currency: 
 curl -X POST \
  http://0.0.0.0:8000/convert_currency/ \
  -H 'Content-Type: application/json' \
  -d '{
	"amount": 1200,
	"currencyFrom": "USD",
	"currencyTo": "EUR"
}'

Example of request to add currency:

  curl -X POST \
  http://0.0.0.0:8000/add_currency/ \
  -H 'Content-Type: application/json' \
  -d '{
	"currency": "USD"
}'

Currencies are updated each 24 hours (celery task).

 To launch project use docker-compose. 
 In the app directory 
  - docker-compose build
  - docker-compose up
  
 App will be running on http://0.0.0.0:8000
