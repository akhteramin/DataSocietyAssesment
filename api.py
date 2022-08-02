from flask import Flask
from flask import request
import requests
import json
import time
import urllib.request
import urllib.error

app = Flask(__name__)

@app.route('/weather/<longitude>/<latitude>', methods = ['GET'])

def getData(longitude = None, latitude = None):

    url = "https://api.weather.gov/points/"+longitude+","+latitude
    try:
        response = requests.get(url)
        content = response.json()


        try:
            responseForecast = requests.get(content['properties']['forecast'])
            contentForecast = responseForecast.json()

            finalResponse = json.dumps(contentForecast['properties']['periods'])

        except requests.exceptions.Timeout:
            return "Timeout"
        # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
            return "Too Many Redirection"
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except:
            return {"Status": "422", "Message": "Error in Longitude and Latitude"}

    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        return "Timeout"

    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        return "Too Many Redirection"

    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except:
        return {"Status": "422", "Message": "Error in Longitude and Latitude"}

    return finalResponse


if __name__ == "__main__":
    app.run(host='0.0.0.0')
