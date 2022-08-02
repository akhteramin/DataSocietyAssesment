from flask import Flask
from flask import request
import json
import time
app = Flask(__name__)

@app.route('/weather/', methods = ['GET'])

def getData():
    print("data")
    return 'JSON data posted'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
