from mongoengine import connect

from app.config import Config
from app.parsers.parser_manager import ParserManager


connect(Config.DB_ALIAS, alias='default', host='mongo')


def run():
    parser_manager = ParserManager()
    parser_manager.run()


if __name__ == '__main__':
    run()
