import os

from mongoengine import connect, disconnect

from app.config import Config
from app.parsers.parser_manager import ParserManager

disconnect()
connect(Config.DB_NAME, alias='default', host=os.getenv('MONGODB_HOST', ''))


def run():
    parser_manager = ParserManager()
    parser_manager.run()


if __name__ == '__main__':
    run()
