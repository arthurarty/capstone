from flask import Blueprint, jsonify, request, abort
from sqlalchemy.exc import DatabaseError, DataError

from app.models.actor import Actor
from utils.query_all import query_all


bp = Blueprint('actors', __name__, url_prefix='/actors')


@bp.route('', methods=['GET'])
def get_actors():
    """Get all actors"""
    actor_list = query_all(Actor)
    return jsonify({
        "success": True,
        "actors": actor_list
    })


@bp.route('', methods=['POST'])
def create_actor():
    """Adds a new actor given
    age, name and gender
    """
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
        actor_list = query_all(Actor)
        return jsonify({
            'success': True,
            'created': new_actor.id,
            'actors': actor_list,
            'total_actors': len(actor_list)
        }), 201
    except DatabaseError:
        abort(422)


@bp.route('<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    """Delete an actor or return 404
    if actor with given id does not exist
    """
    actor = Actor.find(actor_id)

    if actor is None:
        abort(404)

    actor.delete()
    actor_list = query_all(Actor)
    return jsonify({
            'success': True,
            'deleted': actor_id,
            'actor_list': actor_list
        })
