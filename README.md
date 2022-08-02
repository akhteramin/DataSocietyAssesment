# Coding Challenge
## What's Provided
Write a weather-forecasting application that takes geographic US latitude/longitude values as input and presents the weather from a point in time at the given location(s). Use a language and presentation method of your choice. The design of the application, as well as any additional information you’d like to display, is up to you. This application should:
* Accept geographic US latitude/longitude values as input
    *  For example: 38.2527° N, 85.7585° W
    * Retrieve weather data using this free weather service: API Web Service (https://www.weather.gov/documentation/services-web-api&sa=D&source=calendar&ust=1641768438693965&usg=AOvVaw3OWCV8Z2DjkIpuF6eXz_L2)
* Your chosen tools will dictate your presentation method, but the key to this requirement is that the end-user receives the resulting forecast data. This could be done via a dynamic web page, command-line output, etc.
### How to Run

* To run this application in development mode, one can run the following command:
`python3 api.py`
* To run this application on an nginx server, we need to execute this following command:
`gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app`.

### How to Use
The following endpoints are available to use:
```
* CREATE
    * HTTP Method: POST 
    * URL: localhost:8080/user
    * PAYLOAD: User
    * RESPONSE: User
* READ
    * HTTP Method: GET 
    * URL: localhost:8080/weather/{longitude}/{latitude}
    * RESPONSE: Forecast

```
The User has a JSON schema of:
```json
{
  "type":"User",
  "properties": {
    "useerId": {
      "type": "string"
    },
    "username": {
      "type": "string"
    },
    "password": {
          "type": "string"
    },
    
  }
}
```
For all endpoints that require an "id" in the URL, this is the "employeeId" field.

## What to Implement

### Task 1
Present the “temperature” value for “Wednesday Night” at the input location


## Delivery
Along with the source code, include a README.md file in Markdown format which documents your solution and how to use it. Deliver the application via shared git repository (e.g. GitHub, BitBucket).
