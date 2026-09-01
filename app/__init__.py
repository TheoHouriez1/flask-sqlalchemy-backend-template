from flask import Flask, jsonify

from config import config_by_name
from app.extensions import db, migrate, cors


def create_app(env_name="development"):
    """
    Application factory.
    env_name: "development" | "production" | "testing"
    """
    app = Flask(__name__)
    app.config.from_object(config_by_name[env_name])

    # --- Extensions ---
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # --- Blueprints ---
    from app.routes.health import bp as health_bp
    from app.routes.users import bp as users_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)

    # --- Import des modèles pour que Flask-Migrate les détecte ---
    from app.models import user  # noqa: F401

    # --- Gestion d'erreurs globale ---
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app
