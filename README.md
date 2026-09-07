# flask-sqlalchemy-backend-template

Template perso pour démarrer un backend Flask + SQLAlchemy rapidement,
sans reperdre 30 minutes à remonter l'architecture à chaque projet.

## Stack

- Flask (application factory + Blueprints)
- Flask-SQLAlchemy (ORM)
- Flask-Migrate (migrations façon Alembic)
- Flask-Cors
- python-dotenv (config par environnement)
<<<<<<< HEAD
=======
- PostgreSQL (via psycopg2-binary) — DATABASE_URL est **obligatoire**, pas de fallback SQLite
>>>>>>> e76873c (push dynamique routes and dynamique models)

## Structure

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

## Utilisation pour un nouveau projet

```bash
# 1. Cloner le template
<<<<<<< HEAD
git clone <url-de-ce-repo> mon-nouveau-projet
cd mon-nouveau-projet
rm -rf .git && git init   # repartir sur un historique propre

# 2. Créer et activer le venv
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
=======
git clone <flask-sqlalchemy-backend-template> mon-nouveau-projet
cd mon-nouveau-projet

# 2. Créer et activer le venv
python -m venv venv
source venv/Scripts/activate      # Windows: venv\Scripts\activate
>>>>>>> e76873c (push dynamique routes and dynamique models)

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer l'environnement
<<<<<<< HEAD
cp .env.example .env
# éditer .env si besoin (DATABASE_URL, SECRET_KEY...)

# 5. Initialiser les migrations et la base
=======
cp .env.example .envpython --version
# éditer .env : DATABASE_URL (obligatoire), SECRET_KEY...

# 5. Lancer le container Postgres (si docker-compose.yml présent)
docker compose up -d

# 6. Initialiser les migrations et la base
>>>>>>> e76873c (push dynamique routes and dynamique models)
flask db init
flask db migrate -m "initial migration"
flask db upgrade

<<<<<<< HEAD
# 6. Lancer le serveur
=======
# 7. Lancer le serveur
>>>>>>> e76873c (push dynamique routes and dynamique models)
python run.py
```

L'API tourne sur http://localhost:5000, avec `/health` comme route de test.

## Ajouter un nouveau domaine (ex: "products")

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

## Notes

- Le modèle `User` et le Blueprint `users` servent d'exemple concret
  (CRUD complet) — à supprimer ou adapter selon le projet.
- Pense à changer `SECRET_KEY` en prod (jamais la valeur par défaut).
<<<<<<< HEAD
- `SQLALCHEMY_DATABASE_URI` : SQLite par défaut en dev, remplacer par
  une URL PostgreSQL/MySQL via `DATABASE_URL` en prod.
=======
- `DATABASE_URL` est **requise** dans `.env` (dev, test, prod) — l'app
  refuse de démarrer sans elle (`RuntimeError` volontaire, fail fast).
  Format : `postgresql://user:password@host:5432/nom_db`.
>>>>>>> e76873c (push dynamique routes and dynamique models)
