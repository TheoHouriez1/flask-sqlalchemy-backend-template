from flask import Flask, jsonify

from config import config_by_name
from app.extensions import db, migrate, cors


def create_app(env_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env_name])

    # --- Extensions ---
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # --- Blueprints ---
    from app.routes import register_blueprints
    register_blueprints(app)

    from app import models

    # --- Gestion d'erreurs globale ---
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app
