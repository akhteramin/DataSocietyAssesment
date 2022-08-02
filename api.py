from flask import Flask,  render_template
from flask import request
import requests
import json
import time
import urllib.request
import urllib.error

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", data="data1", data2="data2")





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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
