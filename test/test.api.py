import unittest
import requests
import json

class TestWeatherForecastRequests(unittest.TestCase):
    def test_weather(self):
        response = requests.get('http://0.0.0.0:5000/documented_api/weather_api/weather/48.7456/-97.034')
        # Retrieving Response Data
        forecast_data = json.loads(response.json())

        # Opening JSON file
        f = open('test_output.json')

        # returns JSON object as
        # a dictionary
        test_content = json.load(f)



        self.assertEqual(forecast_data, test_content)



if __name__ == "__main__":
    unittest.main()