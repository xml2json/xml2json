from flask import Flask, request
import flask, os
from flask.ext.rq import RQ
from workers import *

app = Flask(__name__)

RQ(app)

@app.route("/api/game/<int:game_id>", methods=['GET'])
def find_game_id(game_id):
    try:
        json = eventsJSONWithGameId(game_id)
    except:
        return flask.jsonify({'code':404, 'msg':'Game id not found!'})
    return flask.jsonify({'code':200,'msg':'', 'result': json})

@app.route("/api/save", methods=['POST'])
def save_game_result():
    xml = request.form.get('event-feed', '')
    saveEventFeed(xml)
    return flask.jsonify({'code':200,'msg':'Processing feed'})

if __name__ == "__main__":
    app.debug = (os.environ.get('XML2JSON_DEBUG') or "").lower() == "true"
    app.run()
