# match.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum

db = SQLAlchemy()

class MatchStatus(enum.Enum):
    """
    Enumeración para representar los posibles estados de un encuentro
    """
    PENDING = "Pending"
    COMPLETED = "Completed"

class Match(db.Model):
    """
    Modelo de Encuentro para la base de datos
    """
    __tablename__ = 'matches'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Identificador único para cada encuentro
    player1_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)  # ID del primer jugador
    player2_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)  # ID del segundo jugador
    player1_score = db.Column(db.Integer, default=0)  # Puntuación del primer jugador
    player2_score = db.Column(db.Integer, default=0)  # Puntuación del segundo jugador
    status = db.Column(Enum(MatchStatus), default=MatchStatus.PENDING)  # Estado del encuentro (pendiente o completado)
    date = db.Column(db.DateTime)  # Fecha del encuentro

    player1 = relationship("User", foreign_keys=[player1_id])  # Relación con el primer jugador
    player2 = relationship("User", foreign_keys=[player2_id])  # Relación con el segundo jugador

    def __repr__(self):
        return f"<Match(id={self.id}, player1_id={self.player1_id}, player2_id={self.player2_id}, player1_score={self.player1_score}, player2_score={self.player2_score}, status={self.status}, date={self.date})>"