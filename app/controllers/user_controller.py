# user_controller.py
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from ..models import User
from ..database import db_session

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/api/users', methods=['GET'])
def get_users():
    """
    Obtener todos los usuarios
    """
    users = db_session.query(User).all()
    return jsonify([user.to_dict() for user in users])

@user_blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Obtener un usuario por su ID
    """
    user = db_session.query(User).filter(User.id == user_id).first()
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'message': 'User not found'}), 404

@user_blueprint.route('/api/users', methods=['POST'])
def create_user():
    """
    Crear un nuevo usuario
    """
    data = request.get_json()
    new_user = User(**data)
    
    try:
        db_session.add(new_user)
        db_session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db_session.rollback()
        return jsonify({'message': 'Error: Email is already in use'}), 400

@user_blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Actualizar un usuario existente
    """
    user = db_session.query(User).filter(User.id == user_id).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    
    db_session.commit()
    
    return jsonify({'message': 'User updated successfully'})

@user_blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Eliminar un usuario
    """
    user = db_session.query(User).filter(User.id == user_id).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    db_session.delete(user)
    db_session.commit()
    
    return jsonify({'message': 'User deleted successfully'})