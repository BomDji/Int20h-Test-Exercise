import os

from flask import Flask
from flask_cors import CORS

from mongoengine import connect

from .api import api_bp
from .config import Config


# app set up and add blueprint
app = Flask(__name__)
app.config.from_object('app.config.Config')

# enable CORS
CORS(app)

app.register_blueprint(api_bp)
connect(Config.DB_NAME, alias='default', host=os.getenv('MONGODB_HOST', ''))

# logger set up
app.logger.info('>>> {}'.format(Config.FLASK_ENV))
