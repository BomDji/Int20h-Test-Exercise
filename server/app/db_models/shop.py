from mongoengine import *


class Shop(Document):
    name = StringField(unique=True)

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name
