from flask import Blueprint, jsonify, request
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
