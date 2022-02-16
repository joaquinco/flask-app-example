import runpy
import os

from web_app import app, init_db

init_db()
os.environ['FLASK_APP'] = 'web_app'
runpy.run_module('flask')
