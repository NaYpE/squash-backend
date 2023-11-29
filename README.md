# Backend para la Aplicación de Tabla de Posiciones de Squash

## Contenido
1. [Información General](#información-general)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Modelos de base de datos](#modelos-de-base-de-datos)
4. [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)
5. [Uso de Docker](#uso-de-docker)
6. [Estructura del Proyecto](#estructura-del-proyecto)
7. [API Endpoints](#api-endpoints)
8. [Contribución](#contribución)
9. [Licencia](#licencia)

## Información General

Este es el backend de la aplicación web de tabla de posiciones para el juego de squash. La aplicación permite a los usuarios (jugadores de squash) competir uno contra uno y actualiza automáticamente la tabla de posiciones en función de los resultados de los encuentros.

## Tecnologías Utilizadas

- Python: Lenguaje de programación principal.
- Flask: Marco web ligero para el desarrollo rápido de aplicaciones web.
- SQLAlchemy: Biblioteca para interactuar con la base de datos.
- SQLite: Sistema de gestión de bases de datos utilizado para almacenar los datos de la aplicación.
- Docker
- Pytest: Marco de pruebas para Python.

## Modelos de base de datos

Tenemos dos modelos principales en nuestra base de datos:

- `Jugador`: Cada jugador tiene un `nombre` y `puntos`.
- `Encuentro`: Cada encuentro tiene dos jugadores (`jugador1_id` y `jugador2_id`) y un `ganador_id`.

Después de cada encuentro, la tabla de posiciones se actualiza automáticamente.


## Configuración del Entorno de Desarrollo

1. **Clonar el Repositorio:**
   ```bash
   git clone git@github.com:NaYpE/squash-backend.git
    ```
2. **Instalar Dependencias:**
    ```bash
    cd squash-backend
    pip install -r requirements.txt
    ```
3. **Configurar la Base de Datos:**
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```
4. **Ejecutar la Aplicación:**
    ```bash
    flask run
    ```
La aplicación estará disponible en http://localhost:5000.

## Uso de Docker

Para construir y ejecutar la aplicación usando Docker, sigue estos pasos:

1. Construye la imagen Docker:

    ```bash
    docker-compose build
    ```
2. Ejecuta la aplicación:

    ```bash
    docker-compose up
    ```

## Estructura del Proyecto

- **`app/`**: Contiene el código fuente de la aplicación.
    - **models/**: Definiciones de modelos de base de datos.
    - **routes/**: Rutas de la aplicación.
    - **templates/**: Plantillas HTML si es una aplicación de renderización de vistas.
- **`migrations/`**: Scripts de migración para la base de datos.
- **`config.py`**: Configuración de la aplicación.
- **`run.py`**: Archivo de entrada para ejecutar la aplicación.

## API Endpoints

- ``GET`` **/api/usuarios**: Obtener la lista de usuarios.
- `POST` **/api/encuentros**: Crear, actualizar y obtener información sobre los encuentros.
- `GET` **/api/tablaposiciones**: Obtener la tabla de posiciones actualizada.

## Contribución

¡Siéntete libre de contribuir! Abre un problema o envía una solicitud de extracción con tus mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.