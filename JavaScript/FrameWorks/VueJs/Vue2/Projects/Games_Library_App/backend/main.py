from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/')
def greeting():
    return("Hello, World")

@app.route('/shark')
def shark():
    return("Shark 🦈!")

GAMES = [
    {
        "id": uuid.uuid4().hex,
        "title": "2K21",
        "genre": "sports",
        "played": True
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Evil Within",
        "genre": "horror",
        "played": False
    },
    {
        "id": uuid.uuid4().hex,
        "title": "The Last of Us",
        "genre": "survival",
        "played": True
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Days Gone",
        "genre": "horror/survival",
        "played": False
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Mario",
        "genre": "retro",
        "played": True
    },
]

# The GET and POST route handler
@app.route("/games", methods=["GET", "POST"])
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = "Game Added!"
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)

# The PUT and DELETE rounte handler
@app.route('/games/<games_id>', methods=["PUT", "DELETE"])
def single_game(games_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(games_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = "Game Updated!"

    if request.method == "DELETE":
        remove_game(games_id)
        response_object['message'] = "Game removed!"
    return jsonify(response_object)

# Removing the game to update
def remove_game(games_id):
    for game in GAMES:
        if game['id'] == games_id:
            GAMES.remove(game)
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
