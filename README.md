# Flask SQLAlchemy Backend Template

<p align="center">
   <strong>Une base propre et pragmatique pour lancer rapidement une API Flask.</strong>
</p>

<p align="center">
   <a href="https://github.com/TheoHouriez1/flask-sqlalchemy-backend-template"><img src="https://img.shields.io/github/last-commit/TheoHouriez1/flask-sqlalchemy-backend-template?style=flat-square&label=derni%C3%A8re%20mise%20%C3%A0%20jour" alt="Dernière mise à jour"></a>
   <a href="https://github.com/TheoHouriez1/flask-sqlalchemy-backend-template/commits/main"><img src="https://img.shields.io/github/commit-activity/y/TheoHouriez1/flask-sqlalchemy-backend-template?style=flat-square&label=activit%C3%A9" alt="Activité des commits"></a>
   <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-3.0.3-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask 3.0.3"></a>
   <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-15%2B-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL 15+"></a>
   <a href="https://github.com/TheoHouriez1/flask-sqlalchemy-backend-template"><img src="https://img.shields.io/github/repo-size/TheoHouriez1/flask-sqlalchemy-backend-template?style=flat-square&label=taille%20du%20d%C3%A9p%C3%B4t" alt="Taille du dépôt"></a>
</p>

Ce dépôt sert de template pour démarrer un backend Flask + SQLAlchemy sans
reconstruire la même architecture à chaque projet.

## Pourquoi ce template ?

- Une **application factory** prête à l'emploi
- Des **Blueprints** organisés par domaine
- SQLAlchemy et Flask-Migrate déjà configurés
- Une configuration par environnement avec `.env`
- PostgreSQL comme base de données de référence, sans fallback SQLite

## Stack

| Technologie | Rôle |
| --- | --- |
| Flask 3.0.3 | API, application factory et Blueprints |
| Flask-SQLAlchemy 3.1.1 | ORM et accès aux données |
| Flask-Migrate 4.0.7 | Migrations Alembic |
| Flask-Cors 4.0.1 | Gestion du CORS |
| PostgreSQL | Base de données relationnelle |
| python-dotenv 1.0.1 | Variables d'environnement |

## Structure du projet

```
app/
├── __init__.py       # create_app() : factory principale
├── extensions.py     # instances partagées (db, migrate, cors)
├── models/           # tables SQLAlchemy
├── routes/           # Blueprints (un fichier = un domaine)
├── schemas/          # sérialisation / validation (Marshmallow, Pydantic...)
└── services/         # logique métier, pour garder les routes légères
config.py             # config Dev / Testing / Production
run.py                # point d'entrée
requirements.txt
.env.example
```

## Démarrage rapide

```bash
# 1. Cloner le template
git clone https://github.com/TheoHouriez1/flask-sqlalchemy-backend-template backend
cd backend

# 2. Créer et activer le venv
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer l'environnement
cp .env.example .env
# éditer .env : DATABASE_URL (obligatoire), SECRET_KEY...

# 5. Lancer PostgreSQL si nécessaire (par exemple via Docker)
docker compose up -d

# 6. Initialiser les migrations et la base
flask db init
flask db migrate -m "initial migration"
flask db upgrade

# 7. Lancer le serveur
python run.py
```

L'API tourne sur http://localhost:5000, avec `/health` comme route de test.

## Ajouter un domaine

Exemple avec un domaine `products` :

1. Créer le modèle dans `app/models/product.py`
2. Créer le Blueprint dans `app/routes/products.py`
3. L'importer et l'enregistrer dans `app/__init__.py` :
   ```python
   from app.routes.products import bp as products_bp
   app.register_blueprint(products_bp)
   ```
4. Importer le modèle dans `app/__init__.py` (section "Import des modèles")
   pour que Flask-Migrate le détecte :
   ```python
   from app.models import product  # noqa: F401
   ```
5. Générer et appliquer la migration :
   ```bash
   flask db migrate -m "add product model"
   flask db upgrade
   ```

## Configuration

- Le modèle `User` et le Blueprint `users` servent d'exemple concret
  (CRUD complet) — à supprimer ou adapter selon le projet.
- Pense à changer `SECRET_KEY` en prod (jamais la valeur par défaut).
- `DATABASE_URL` est **requise** dans `.env` (dev, test, prod) — l'app
  refuse de démarrer sans elle (`RuntimeError` volontaire, fail fast).
  Format : `postgresql://user:password@host:5432/nom_db`.

## Routes disponibles

| Méthode | Route | Description |
| --- | --- | --- |
| `GET` | `/health` | Vérifie que l'API répond |
| `GET` | `/users` | Liste les utilisateurs |
| `POST` | `/users` | Crée un utilisateur |
| `GET` | `/users/<id>` | Récupère un utilisateur |
| `PUT` | `/users/<id>` | Met à jour un utilisateur |
| `DELETE` | `/users/<id>` | Supprime un utilisateur |

## Licence

Ce template est destiné à être copié et adapté à vos projets.
