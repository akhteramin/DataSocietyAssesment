# from flask import Flask,  render_template
# import requests
# import json
# from flask_restx import Api
# from flask_restplus import Resource
#
# app = Flask(__name__)
#
# api = Api(app)
#
#
# # @api.route('/index')
# # def index():
# #     return render_template("index.html", data="data1", data2="data2")
#
#
# @api.route('/weather/<longitude>/<latitude>')
#
# class DataAPI(Resource):
#     def get(self, longitude = None, latitude = None):
#
#         url = "https://api.weather.gov/points/"+longitude+","+latitude
#         try:
#             initialResponse = requests.get(url)
#             forecastEndPointContent = initialResponse.json()
#
#
#             try:
#                 responseForecast = requests.get(forecastEndPointContent['properties']['forecast'])
#                 contentForecast = responseForecast.json()
#
#                 finalResponse = json.dumps(contentForecast['properties']['periods'])
#
#             except requests.exceptions.Timeout:
#                 return {"Message": "Request Timeout"}
#             # Maybe set up for a retry, or continue in a retry loop
#             except requests.exceptions.TooManyRedirects:
#             # Tell the user their URL was bad and try a different one
#                 return {"Status": "400", "Message": "Bad URL Request"}
#
#             except requests.exceptions.RequestException as e:
#                 # catastrophic error. bail.
#                 raise SystemExit(e)
#
#             except requests.exceptions.HTTPError as err:
#                 raise SystemExit(err)
#
#             except KeyError as e:
#                 return {"Status": "422", "Message": "Invalid Longitude and Latitude"}
#
#         except requests.exceptions.Timeout:
#             # Maybe set up for a retry, or continue in a retry loop
#             return {"Message": "Request Timeout"}
#
#         except requests.exceptions.TooManyRedirects:
#             # Tell the user their URL was bad and try a different one
#             return {"Status": "400", "Message": "Bad URL Request"}
#
#         except requests.exceptions.RequestException as e:
#             # catastrophic error. bail.
#             raise SystemExit(e)
#         except requests.exceptions.HTTPError as err:
#             raise SystemExit(err)
#         except KeyError as e:
#             return {"Status": "422", "Message": "Invalid Longitude and Latitude"}
#
#         return finalResponse
#
#
# @api.route('/weather/<email>')
# class AuthAPI(Resource):
#
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
