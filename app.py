from flask import Flask, jsonify
from utils import *
import json

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False



@app.route('/movie/<title>')
def get_by_title(title):
    return movie_by_title(title)


@app.route('/movie/<int:year1>/to/<int:year2>')
def get_by_years(year1: int, year2: int):
    return jsonify(movies_by_year(year1, year2))


@app.route('/rating/<category>')
def get_by_rating(category):
    return jsonify(movies_by_rating(category))


@app.route('/genre/<genre>')
def get_by_genre(genre):
    return jsonify(fresh_movies_by_genre(genre))


if __name__ == "__main__":
    app.run(debug=True)
