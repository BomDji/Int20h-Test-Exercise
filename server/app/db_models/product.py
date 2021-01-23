from mongoengine import *
from .shop import Shop


class Product(Document):
    shop = ReferenceField(Shop, reverse_delete_rule=CASCADE)

    name = StringField()
    description = StringField()

    price = FloatField()
    currency = StringField()
    price_history = ListField()

    link = StringField()

    img_link = StringField()

    category_tag = StringField()
