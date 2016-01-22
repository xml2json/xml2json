from flask import Flask
import flask, os
from flask.ext.rq import RQ
from workers import *

app = Flask(__name__)

RQ(app)

@app.route("/api/game/<int:game_id>", methods=['GET'])
def find_game_id(game_id):
    f = {'err':'not implemented'}
    sleepForThreeSeconds.delay()
    return flask.jsonify(**f)

@app.route("/api/save", methods=['POST'])
def save_game_result():
    f = {'err':'not implemented'}
    return flask.jsonify(**f)

if __name__ == "__main__":
    app.debug = (os.environ.get('XML2JSON_DEBUG') or "").lower() == "true"
    app.run()
