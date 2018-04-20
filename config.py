import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "N265/W;'Nk@Bgh0BVCVypDKy6)y?ui"
