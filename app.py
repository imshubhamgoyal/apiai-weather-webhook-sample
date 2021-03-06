#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "getmarks":
        return {
                "speech": "no good"
                "displayText": "no good",
                # "data": data,
                # "contextOut": [],
                "source": "apiai-weather-webhook-sample"
                }
    baseurl = "http://parkingapp.online/simple_query.php"
    yql_query = makeYqlQuery(req)
    if yql_query is None:
        return {
            "speech": "no good"
            "displayText": "no good",
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
                }
    yql_url = baseurl + "&format=json"
    result = urlopen(yql_url).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res


def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    student = parameters.get("student")
    if city is None:
        return {
            "speech": "no good"
            "displayText": "no good",
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
               }
    return "select * from scores where text='" + student + "')"


def makeWebhookResult(data):
    query = data.get('1')
    if query is None:
        return {
            "speech": "no good"
            "displayText": "no good",
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
            }
    algoresult = query.get('Algorithm')
    if result is None:
        return {
            "speech": "no good"
            "displayText": "no good",
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
                }
    
    speech = "Marks in algorithm is " + algoresult
        

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
