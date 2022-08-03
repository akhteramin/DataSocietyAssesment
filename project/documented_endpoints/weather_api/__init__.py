from flask import request
from flask_restplus import Namespace, Resource, fields
import requests
import json


namespace = Namespace('weather_api', 'Weather Related API')


@namespace.route('/weather/<longitude>/<latitude>')

class DataAPI(Resource):
    def get(self, longitude = None, latitude = None):

        url = "https://api.weather.gov/points/"+longitude+","+latitude
        try:
            initialResponse = requests.get(url)
            forecastEndPointContent = initialResponse.json()


            try:
                responseForecast = requests.get(forecastEndPointContent['properties']['forecast'])
                contentForecast = responseForecast.json()

                finalResponse = json.dumps(contentForecast['properties']['periods'])

            except requests.exceptions.Timeout:
                return {"Message": "Request Timeout"}
            # Maybe set up for a retry, or continue in a retry loop
            except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
                return {"Status": "400", "Message": "Bad URL Request"}

            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                raise SystemExit(e)

            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)

            except KeyError as e:
                return {"Status": "422", "Message": "Invalid Longitude and Latitude"}

        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {"Message": "Request Timeout"}

        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {"Status": "400", "Message": "Bad URL Request"}

        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except KeyError as e:
            return {"Status": "422", "Message": "Invalid Longitude and Latitude"}

        return finalResponse

