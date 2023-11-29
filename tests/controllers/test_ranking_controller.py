import json
import pytest
from flask import Flask
from flask_testing import TestCase
from app import create_app
from models import Ranking, db

class TestRankingController(TestCase):
    def create_app(self):
        # Create an instance of the application for testing
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        # Create database tables before each test
        db.create_all()

    def tearDown(self):
        # Remove database tables after each test
        db.session.remove()
        db.drop_all()

    def test_get_ranking(self):
        # Create a test ranking
        test_ranking = Ranking(id=1, name='Test Ranking')
        db.session.add(test_ranking)
        db.session.commit()

        # Make a GET request to the /api/rankings/<ranking_id> route
        response = self.client.get('/api/rankings/1')

        # Verify the status code and response content
        assert response.status_code == 200
        assert b'Test Ranking' in response.data

    def test_get_nonexistent_ranking(self):
        # Make a GET request to a non-existent ranking ID
        response = self.client.get('/api/rankings/999')

        # Verify the status code and error message in the response
        assert response.status_code == 404
        assert b'Ranking not found' in response.data

if __name__ == '__main__':
    pytest.main()