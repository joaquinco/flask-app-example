from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .views import pages

app = Flask('exercice')
app.register_blueprint(pages)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
db = SQLAlchemy(app)


def init_db():
    import web_app.models

    db.create_all()
