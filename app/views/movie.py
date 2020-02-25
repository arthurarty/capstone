from flask import Blueprint, abort, jsonify, request
from sqlalchemy.exc import DatabaseError, DataError

from app.models.movie import Movie
from utils.query_all import query_all

bp = Blueprint('movies', __name__, url_prefix='/movies')


@bp.route('', methods=['GET'])
def get_movies():
    """Get all movies"""
    movie_list = query_all(Movie)
    return jsonify({
        "success": True,
        "movies": movie_list
    })


@bp.route('', methods=['POST'])
def create_movie():
    """Adds a new movie"""
    body = request.get_json()
    validated_body = {}
    required_fields = ['title', 'release_date']
    for field in required_fields:
        resp = body.get(field, None)
        if resp is None:
            abort(400)
        validated_body[field] = resp

    try:
        new_movie = Movie(
            title=validated_body['title'],
            release_date=validated_body['release_date'])
        new_movie.insert()
        movie_list = query_all(Movie)
        return jsonify({
            'success': True,
            'created': new_movie.id,
            'movies': movie_list,
            'total_movies': len(movie_list)
        }), 201
    except DatabaseError:
        abort(422)
