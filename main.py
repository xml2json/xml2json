from flask import Flask, request
import flask, os
from flask.ext.rq import RQ
from flask.ext.api import status
from workers import *
from xml.etree import ElementTree as ET

app = Flask(__name__)

RQ(app)

@app.route("/api/game/<int:game_id>", methods=['GET'])
def find_game_id(game_id):
    try:
        json = eventsJSONWithGameId(game_id)
        return flask.jsonify({'message':'', 'result': json}), status.HTTP_200_OK
    except:
        return flask.jsonify({'message':'game id not found!'}), status.HTTP_404_NOT_FOUND

@app.route("/api/save", methods=['POST'])
def save_game_result():
    xml = request.data
    try:
        ET.fromstring(xml)
    except:
        return flask.jsonify({'message':'invalid xml file'}), status.HTTP_400_BAD_REQUEST
    saveEventFeed(xml)
    return flask.jsonify({'message':'processing feed'}), status.HTTP_200_OK

if __name__ == "__main__":
    app.run()
