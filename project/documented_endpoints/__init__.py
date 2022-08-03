# blueprints/documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api
from project.documented_endpoints.weather_api import namespace as weather_forecast_api

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='Weather API Remo',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc'
)

api_extension.add_namespace(weather_forecast_api)