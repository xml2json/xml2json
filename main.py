from flask import Flask
import flask

app = Flask(__name__)

@app.route("/api/game/<int:game_id>", methods=['GET'])
def find_game_id(game_id):
    f = {'key':'hello'}
    return flask.jsonify(**f)

if __name__ == "__main__":
    app.run()
