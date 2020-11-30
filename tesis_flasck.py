'''
Created on Sep 18, 2020

@author: Gabriel Torrandella
'''
from flask import Flask, json, jsonify
from flask.globals import request
from flask.wrappers import Response

from tesis_rejson_connector import Connector

app = Flask(__name__)
co = Connector()

@app.route('/logger', methods = ['POST'])
def api_logger():
    if 'Content-Type' in request.headers.keys():
        if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            co.saveLog(request.form, "TEST")
            return Response(status = 200)
        else:
            return Response(status = 400)
                
    else:
        return Response(status = 400)

@app.route('/logger/<string:id>', methods = ['GET'])
def api_logger_id():
    if 'Content-Type' in request.headers.keys():
        if request.headers['Content-Type'] == 'application/json':
            logJson = request.json
            print(logJson)
            try:
                co.saveLog(logJson, 'aaa')
                return Response(status = 200)
            except:
                return Response(400)
        else:
            return Response(400)
                
    else:
        return Response(status = 400)


if __name__ == "__main__":
    app.run(host='0.0.0.0')