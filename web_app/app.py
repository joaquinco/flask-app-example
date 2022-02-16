from flask import Flask

from .views import pages

app = Flask('exercice')
app.register_blueprint(pages)
