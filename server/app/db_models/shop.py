from mongoengine import *


class Shop(Document):
    name = StringField(unique=True)
