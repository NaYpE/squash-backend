# test_user_controller.py
import json
import pytest
from flask import Flask
from flask_testing import TestCase
from app import create_app
from models import User, db

class TestUserController(TestCase):
    def create_app(self):
        # Crear una instancia de la aplicación para las pruebas
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        # Crear las tablas de la base de datos antes de cada prueba
        db.create_all()

    def tearDown(self):
        # Eliminar las tablas de la base de datos después de cada prueba
        db.session.remove()
        db.drop_all()

    def test_get_users(self):
        # Crear un usuario de prueba
        test_user = User(name='Test', email='test@example.com')
        db.session.add(test_user)
        db.session.commit()

        # Realizar una solicitud GET a la ruta /api/users
        response = self.client.get('/api/users')

        # Verificar el código de estado y el contenido de la respuesta
        assert response.status_code == 200
        assert b'Test' in response.data

    def test_create_user(self):
        # Datos para crear un usuario
        data = {'name': 'New', 'email': 'new@example.com'}

        # Realizar una solicitud POST a la ruta /api/users
        response = self.client.post('/api/users', data=json.dumps(data), content_type='application/json')

        # Verificar el código de estado y el contenido de la respuesta
        assert response.status_code == 201
        assert b'New' in response.data

        # Verificar que el usuario fue creado en la base de datos
        new_user = User.query.filter_by(email='new@example.com').first()
        assert new_user is not None
        assert new_user.name == 'New'

    def test_create_existing_user(self):
        # Crear un usuario de prueba
        test_user = User(name='Test', email='test@example.com')
        db.session.add(test_user)
        db.session.commit()

        # Intentar crear un usuario con el mismo correo electrónico
        data = {'name': 'Another Test', 'email': 'test@example.com'}
        response = self.client.post('/api/users', data=json.dumps(data), content_type='application/json')

        # Verificar que la respuesta tiene un código de estado 400 y un mensaje de error
        assert response.status_code == 400
        assert b'Error: User with this email already exists' in response.data

    def test_get_nonexistent_user(self):
        # Intentar obtener un usuario que no existe
        response = self.client.get('/api/users/999')

        # Verificar que la respuesta tiene un código de estado 404 y un mensaje de error
        assert response.status_code == 404
        assert b'Error: User not found' in response.data

if __name__ == '__main__':
    pytest.main()