from flask import Blueprint, abort, jsonify, request
from sqlalchemy.exc import DatabaseError, DataError

from app.auth.auth import AuthError, requires_auth
from app.models.movie import Movie
from utils.query_all import query_all

bp = Blueprint('movies', __name__, url_prefix='/movies')


@bp.route('', methods=['GET'])
@requires_auth('get:movies')
def get_movies():
    """Get all movies"""
    movie_list = query_all(Movie)
    return jsonify({
        "success": True,
        "movies": movie_list
    })


@bp.route('', methods=['POST'])
@requires_auth('create:movies')
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


@bp.route('<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movie(movie_id):
    """Edit an existing movie"""
    movie = Movie.find(movie_id)

    if movie is None:
        abort(404)

    body = request.get_json()
    validated_body = {}
    fields = ['title', 'release_date']
    for field in fields:
        resp = body.get(field, None)
        validated_body[field] = resp

    if validated_body['title'] is not None:
        movie.title = validated_body['title']
    if validated_body['release_date'] is not None:
        movie.release_date = validated_body['release_date']

    try:
        movie.update()
        movie_list = query_all(Movie)
        return jsonify({
            'success': True,
            'movies': movie_list,
        }), 200
    except DatabaseError:
        abort(422)
