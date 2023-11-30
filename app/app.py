from flask import Flask
from controllers.user_controller import user_blueprint
from controllers.ranking_controller import ranking_blueprint
from controllers.match_controller import matches_blueprint
from database import init_db, shutdown_session

app = Flask(__name__)

# Configurar la aplicación para cerrar la sesión después de cada solicitud
app.teardown_appcontext(shutdown_session)

# Registrar los Blueprints en la aplicación
app.register_blueprint(user_blueprint)
app.register_blueprint(ranking_blueprint)
app.register_blueprint(matches_blueprint)

# Ruta de prueba
@app.route('/')
def hello_world():
    return 'Hello, Docker!'

if __name__ == "__main__":
    # Inicializar la base de datos
    init_db()
    
    # Ejecutar la aplicación
    app.run(debug=True)