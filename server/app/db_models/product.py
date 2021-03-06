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

    img_path = StringField(null=True)
    img_link = StringField()

    category_tag = StringField()

    def __repr__(self):
        return f'{self.name} {self.shop} {self.price}'

    def __unicode__(self):
        return f'{self.name} {self.shop} {self.price}'
