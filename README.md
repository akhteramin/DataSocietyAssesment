# Coding Challenge
## What's Provided
Write a weather-forecasting application that takes geographic US latitude/longitude values as input and presents the weather from a point in time at the given location(s). Use a language and presentation method of your choice. The design of the application, as well as any additional information you’d like to display, is up to you. This application should:
* Accept geographic US latitude/longitude values as input
    *  For example: 38.2527° N, 85.7585° W
    * Retrieve weather data using this free weather service: API Web Service (https://www.weather.gov/documentation/services-web-api&sa=D&source=calendar&ust=1641768438693965&usg=AOvVaw3OWCV8Z2DjkIpuF6eXz_L2)
* Your chosen tools will dictate your presentation method, but the key to this requirement is that the end-user receives the resulting forecast data. This could be done via a dynamic web page, command-line output, etc.
### How to Run
* To install all required packages, please run this command:
`pip3 install requirements.txt`
* To run this application in development mode, one can run the following command:
`flask run`
* To run this application on an nginx server, we need to execute this following command:
`gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app`.

### How to Use
The following endpoints are available to use:
```

* READ
    * HTTP Method: GET 
    * URL: http://localhost:5000/documented_api/weather_api/weather/48.7456/-97.034
    * RESPONSE: Weather Forecast

```

Without authentication the application can not be accessed. However, due to time constraint, no API-end authentication has been implemented.

After running the project, the MVP of the weather forecast website can be accessed at this address: `http://localhost:5000/`

Create account using login id and password. After creating the account, using the login credential users will be able to access the page wherein users are allowed to provide `longitude` and `latitude` to generate weather forecast for upcoming week. 

## How to create a table in sqlite from Flask
The steps of table creation are as follows:
1. First create a model. In this project we hav e created a model class in `models.py` titled `WeatherReport`.
```buildoutcfg
class WeatherReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    longitude = db.Column(db.String(10))
    latitude = db.Column(db.String(10))
    day = db.Column(db.String(30))
    temperature = db.Column(db.String(10))
``` 
2. Run the command `flask shell`
3. Now import the model class that represents that represents the table. For example, in this project we have a `WeatherReport` model, for which we want to create a table.
Within flask shell, run these commands:

`>>> from project.models import WeatherReport`

`>>> from project import db`

 `>>> db.create_all()`

After running these the `WeatherReport` table is created in sqlite.
##Swagger Access
After running the application server, one will be able to access the swagger here:
`http://localhost:5000/documented_api/doc`

Swagger interface will be accessible as long as the web application is running. 

##Unit Test
In this project, a minimal version of unit test has been incorporated within test folder. To run the unit test please run the following command in `test` directory:
`python3 test.api.py`
Note that before running the command, the main project need to be running as well.
## What to Implement

### Task 1
Present the “temperature” value for “Wednesday Night” at the input location


## Delivery
Along with the source code, include a README.md file in Markdown format which documents your solution and how to use it. Deliver the application via shared git repository (e.g. GitHub, BitBucket).



## Improvement Scope
* API level Authentication. (Token-based API access)
* Access Control List for Web URL.
* Weather Information should be presented in a more organized manner. More API could be used to make the user interaction interactive.
* Should Have an Error message policy.
* For better project packaging, Docker can be used.