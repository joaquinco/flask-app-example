Exercice Flask App
==================

## Dependencies

- Python >= 3.8

## Structure

- web_app/models.py: where database models are specified.
- web_app/views.py: where endpoints are defined.

## Running

Install dependencies:

```python
pip install -r requirements.txt
```

Run the app:
```python
python flask_app.py run
```

This is a wrapper around flask module so you can use `--help` to see more options.

You can test if it's working properly by going to the browser to the url `http://localhost:5000/healthcheck`.

## Developing

### Adding models

You can add models by extending the `bd.Model` class, importing `bd` from `web_app.app`.

For example:

```python
from .app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

Then, next time you run the flask app the tables will be created to the sqlite databse
automatically.

> Important: the provided startup script does not handle changes to existing models, so adding fields to an existing
model requires to delete the databse (`dev.db` file) or you can handle it with your prefered db migrations mechanism.

### Adding views

Views are the endpoints exposed by your app. You can add them in two ways, by registering them
with the flask app object or grouping them into blueprints.

For example:

```python
from .app import app


@app.route('/test-endpoint', methods=['GET'])
def test_endpoint():
   # create response object
   return response, 200
```
