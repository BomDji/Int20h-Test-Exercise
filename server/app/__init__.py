from flask import Flask

from .api import api_bp
from .config import Config


# app set up and add blueprint
app = Flask(__name__)
app.config.from_object('app.config.Config')

app.register_blueprint(api_bp)


# logger set up
app.logger.info('>>> {}'.format(Config.FLASK_ENV))
