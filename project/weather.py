#weather.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user

import requests
import json

weather = Blueprint('weather', __name__)


@weather.route('/weather', methods=['POST'])
@login_required
def forecast():

    longitude = request.form.get('longitude')
    latitude = request.form.get('latitude')

    url = "http://localhost:5000/documented_api/weather_api/weather/" + longitude + "/" + latitude

    try:
        initialResponse = requests.get(url)
        forecastData = initialResponse.json()



    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        # raise SystemExit(e)
        flash("Request Exception")
        return redirect(url_for('main.home'))

    except requests.exceptions.HTTPError as err:
        flash("Http Error")
        return redirect(url_for('main.home'))

    except KeyError as e:
        flash("Invalid Longitude and Latitude")
        return redirect(url_for('main.home'))

    data = json.loads(forecastData)
    print(data)

    return render_template('weather.html', forecastData=data)
