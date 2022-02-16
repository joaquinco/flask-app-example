from flask import Blueprint

pages = Blueprint('pages', __name__)


@pages.route('/healthcheck')
def healthcheck():
    return 'OK', 200
