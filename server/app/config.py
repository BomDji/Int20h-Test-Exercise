"""
Global Flask Application Setting
 """

import os


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Int20h-test-57K8w6zRtBxs;7!8}tFC=Cgn9')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)

    DB_NAME = 'int20h_test_exercise'
