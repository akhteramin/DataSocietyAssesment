from flask_restplus import Namespace, Resource, fields
import requests
import json


namespace = Namespace('weather_api', 'Weather Related API')


@namespace.route('/weather/<longitude>/<latitude>')

class DataAPI(Resource):
    def get(self, longitude = None, latitude = None):
        # Initial API request to determine the Zone and the API endpoint for that particular Zone
        url = "https://api.weather.gov/points/"+longitude+","+latitude
        try:
            initialResponse = requests.get(url)
            forecastEndPointContent = initialResponse.json()

            try:
                # On success API request for the particular zone identified in response of previous API call
                responseForecast = requests.get(forecastEndPointContent['properties']['forecast'])
                contentForecast = responseForecast.json()

                # Retrieve the Weekly Forecast
                finalResponse = json.dumps(contentForecast['properties']['periods'])

            except requests.exceptions.Timeout as e:
                raise SystemExit(e)

            except requests.exceptions.TooManyRedirects as e:
                raise SystemExit(e)

            except requests.exceptions.RequestException as e:
                raise SystemExit(e)

            except requests.exceptions.HTTPError as e:
                raise SystemExit(e)

            except KeyError as e:
                raise SystemExit(e)

        except requests.exceptions.Timeout as e:
            raise SystemExit(e)

        except requests.exceptions.TooManyRedirects as e:
            raise SystemExit(e)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        except KeyError as e:
            raise SystemExit(e)

        return finalResponse

