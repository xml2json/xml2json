from flask import Flask
import flask

app = Flask(__name__)

@app.route("/api/game/<int:game_id>", methods=['GET'])
def find_game_id(game_id):
    f = {'err':'not implemented'}
    return flask.jsonify(**f)

@app.route("/api/save", methods=['POST'])
def save_game_result():
    f = {'err':'not implemented'}
    return flask.jsonify(**f)

if __name__ == "__main__":
    app.run()
