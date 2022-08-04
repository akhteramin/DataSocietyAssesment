#weather.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user

import requests
import json

from . import base_url

weather = Blueprint('weather', __name__)


@weather.route('/weather', methods=['POST'])
@login_required
def forecast():
    # Reading URL Parameters
    longitude = request.form.get('longitude')
    latitude = request.form.get('latitude')

    # Constructing Weather API URL
    url = base_url + longitude + "/" + latitude


    try:

        # Jsonify the response from Weather API
        response = requests.get(url)
        forecast_data = json.loads(response.json())


    except requests.exceptions.Timeout as e:
        flash("Error: Take too long time")
        return redirect(url_for('main.home'))

    # Maybe set up for a retry, or continue in a retry loop
    except requests.exceptions.TooManyRedirects as e:
        # Tell the user their URL was bad and try a different one
        flash("Error: Too Many Redirection. ")
        return redirect(url_for('main.home'))

    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        # raise SystemExit(e)
        flash("Error: Request Exception. ")
        return redirect(url_for('main.home'))

    except requests.exceptions.HTTPError as e:
        flash("Error: Http Exception. ")
        return redirect(url_for('main.home'))

    except KeyError as e:
        flash("Invalid Longitude and Latitude.")
        return redirect(url_for('main.home'))
    # finally:
    #     flash("Invalid Longitude and Latitude")
    #     return redirect(url_for('main.home'))


    # data = json.loads(forecastData)

    return render_template('weather.html', forecastData=forecast_data)
