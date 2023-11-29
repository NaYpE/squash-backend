# user.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """
    Modelo de Usuario para la base de datos
    """
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Identificador único para cada usuario
    first_name = db.Column(db.String(50), nullable=False)  # Nombre del usuario
    last_name = db.Column(db.String(50), nullable=False)  # Apellido del usuario
    age = db.Column(db.Integer)  # Edad del usuario
    email = db.Column(db.String(120), unique=True, nullable=False)  # Correo electrónico para autenticación y contacto
    password_hash = db.Column(db.String(128))  # Almacenar la contraseña de manera segura (usando un hash)
    score = db.Column(db.Integer, default=0)  # Puntuación o ranking del usuario en la tabla de posiciones
    match_history = db.relationship('Match', backref='user', lazy=True)  # Historial de encuentros del usuario

    @property
    def password(self):
        raise AttributeError('password: campo de solo escritura')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, score={self.score})>"