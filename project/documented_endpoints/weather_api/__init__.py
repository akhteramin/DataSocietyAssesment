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

            except requests.exceptions.Timeout as e:
                raise SystemExit(e)
            # Maybe set up for a retry, or continue in a retry loop
            except requests.exceptions.TooManyRedirects as e:
            # Tell the user their URL was bad and try a different one
                raise SystemExit(e)

            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                raise SystemExit(e)

            except requests.exceptions.HTTPError as e:
                raise SystemExit(e)

            except KeyError as e:
                raise SystemExit(e)

        except requests.exceptions.Timeout as e:
            # Maybe set up for a retry, or continue in a retry loop
            raise SystemExit(e)

        except requests.exceptions.TooManyRedirects as e:
            # Tell the user their URL was bad and try a different one
            raise SystemExit(e)

        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)

        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        except KeyError as e:
            raise SystemExit(e)

        return finalResponse

