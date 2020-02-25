from flask import Blueprint, jsonify, request, abort
from sqlalchemy.exc import DatabaseError, DataError

from app.models.actor import Actor

bp = Blueprint('actors', __name__, url_prefix='/actors')


@bp.route('', methods=['GET'])
def get_actors():
    """Get all actors"""
    actors = Actor.query.all()
    actor_list = [actor.format() for actor in actors]
    return jsonify({
        "success": True,
        "actors": actor_list
    })


@bp.route('', methods=['POST'])
def create_actor():
    """Adds a new actor"""
    body = request.get_json()
    validated_body = {}
    required_fields = ['name', 'age', 'gender']
    for field in required_fields:
        resp = body.get(field, None)
        if resp is None:
            abort(400)
        validated_body[field] = resp

    try:
        new_actor = Actor(
            name=validated_body['name'],
            age=validated_body['age'],
            gender=validated_body['gender'])
        new_actor.insert()
        actors = Actor.query.all()
        actor_list = [actor.format() for actor in actors]
        return jsonify({
            'success': True,
            'created': new_actor.id,
            'actors': actor_list,
            'total_actors': len(actor_list)
        }), 201
    except DatabaseError:
        abort(422)
