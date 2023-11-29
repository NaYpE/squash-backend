# ranking.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Ranking(db.Model):
    """
    Modelo de Ranking para la base de datos
    """
    __tablename__ = 'rankings'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Identificador único para cada entrada en el ranking
    player_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)  # ID del jugador
    score = db.Column(db.Integer, default=0)  # Puntuación del jugador en el ranking

    player = relationship("User")  # Relación con el jugador

    def __repr__(self):
        return f"<Ranking(id={self.id}, player_id={self.player_id}, score={self.score})>"