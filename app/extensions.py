"""
Instances des extensions Flask, centralisées ici pour éviter
les imports circulaires entre app/__init__.py et app/models/*.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
