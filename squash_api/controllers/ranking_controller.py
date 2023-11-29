# ranking_controller.py
from flask import Blueprint, jsonify
from .models import Ranking, User
from .database import db_session

ranking_blueprint = Blueprint('ranking_blueprint', __name__)

@ranking_blueprint.route('/api/rankings', methods=['GET'])
def get_rankings():
    """
    Obtener todos los rankings
    """
    rankings = db_session.query(Ranking).order_by(Ranking.score.desc()).all()
    return jsonify([ranking.to_dict() for ranking in rankings])

@ranking_blueprint.route('/api/rankings/<int:ranking_id>', methods=['GET'])
def get_ranking(ranking_id):
    """
    Obtener un ranking por su ID
    """
    ranking = db_session.query(Ranking).filter(Ranking.id == ranking_id).first()
    if ranking:
        return jsonify(ranking.to_dict())
    else:
        return jsonify({'message': 'Ranking not found'}), 404