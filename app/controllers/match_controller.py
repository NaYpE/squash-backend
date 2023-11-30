# match_controller.py
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from ..models import Match, User
from ..database import db_session
from datetime import datetime

match_blueprint = Blueprint('match_blueprint', __name__)

@match_blueprint.route('/api/matches', methods=['GET'])
def get_matches():
    """
    Obtener todos los encuentros
    """
    matches = db_session.query(Match).all()
    return jsonify([match.to_dict() for match in matches])

@match_blueprint.route('/api/matches/<int:match_id>', methods=['GET'])
def get_match(match_id):
    """
    Obtener un encuentro por su ID
    """
    match = db_session.query(Match).filter(Match.id == match_id).first()
    if match:
        return jsonify(match.to_dict())
    else:
        return jsonify({'message': 'Match not found'}), 404

@match_blueprint.route('/api/matches', methods=['POST'])
def create_match():
    """
    Crear un nuevo encuentro
    """
    data = request.get_json()
    
    player_id_1 = data.get('player_id_1')
    player_id_2 = data.get('player_id_2')

    # Verify both players exist
    if not db_session.query(User).filter(User.id.in_([player_id_1, player_id_2])).count() == 2:
        return jsonify({'message': 'One or both players do not exist'}), 400

    new_match = Match(player_id_1=player_id_1, player_id_2=player_id_2, date=datetime.utcnow())
    
    try:
        db_session.add(new_match)
        db_session.commit()
        return jsonify({'message': 'Match created successfully'})
    except IntegrityError:
        db_session.rollback()
        return jsonify({'message': 'Error: The match already exists'}), 400

@match_blueprint.route('/api/matches/<int:match_id>', methods=['PUT'])
def update_match(match_id):
    """
    Actualizar un encuentro existente
    """
    match = db_session.query(Match).filter(Match.id == match_id).first()
    
    if not match:
        return jsonify({'message': 'Match not found'}), 404
    
    data = request.get_json()
    for key, value in data.items():
        setattr(match, key, value)
    
    db_session.commit()
    
    return jsonify({'message': 'Match updated successfully'})

@match_blueprint.route('/api/matches/<int:match_id>', methods=['DELETE'])
def delete_match(match_id):
    """
    Eliminar un encuentro
    """
    match = db_session.query(Match).filter(Match.id == match_id).first()
    
    if not match:
        return jsonify({'message': 'Match not found'}), 404
    
    db_session.delete(match)
    db_session.commit()
    
    return jsonify({'message': 'Match deleted successfully'})