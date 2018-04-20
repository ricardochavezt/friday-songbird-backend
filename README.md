Esta es nuestra plantilla para backends Python.

Para crear un proyecto de backend Python a partir de esta plantilla, solo hay que seguir los siguientes pasos:

- Hacer fork de este proyecto en Bitbucket
- Crear el virtual environment: `virtualenv venv` (y activarlo con `source venv/bin/activate`)
- Instalar las librerías habituales: `pip install flask sqlalchemy flask-sqlalchemy sqlalchemy-utils flask-migrate flask-script gunicorn psycopg2`
    - Para manejar passwords también hay que instalar 'passlib'
- Crear la BD Postgres local
- Modificar la info en el archivo .env

Y ya estamos. Los endpoints están en `app/__init__.py` y los modelos en `app/models.py`.

(Obviamente luego hay que modificar este README para adaptarlo al nuevo proyecto).

Para empezar a usar Alembic, hay que ejecutar `[foreman run] python manager.py db init`; esto genera el directorio `migrations`.
Para realizar cambios en la BD, se siguen estos pasos:

- cambiar los modelos
- `[foreman run] python manager.py db migrate`
- revisar los scripts generados (en especial si se está utilizando PasswordType, hay que añadir ciertas cosas)  
(Además es bueno ponerle un comentario a la migración generada)
- `[foreman run] python manager.py db upgrade`

**Importante:**: antes de subir la app o cuando se instalen nuevas librerías, se debe ejecutar `pip freeze > requirements.txt`, y el archivo requirements.txt debe incluirse en el repositorio.