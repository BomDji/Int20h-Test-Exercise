"""
REST API Resource Routing
"""

from datetime import datetime
from flask import request, jsonify
from flask_restplus import Resource

from .security import require_auth
from . import api_rest

from mongoengine import connect, Q
from ..db_models.shop import Shop
from ..db_models.product import Product
from ..config import Config

connect(Config.DB_ALIAS, alias='default', host='mongo')


def get_buckwheat_products():
    keywords = ['гречневая', 'гречана']
    cereal_text = 'крупа'
    cereal_name = 'гречка'

    condition1 = Q(name__icontains=cereal_text)
    condition2 = Q(name__icontains=keywords[0]) | Q(name__icontains=keywords[1])
    condition3 = Q(name__icontains=cereal_name)
    return Product.objects((condition1 & condition2) | condition3).order_by('price')


def get_product_data(product):
    return {'shop_name': product.shop.name,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'currency': product.currency,
            'img_link': product.img_link,
            'link': product.link,
            'price_history': product.price_history}


@api_rest.route('/minimum_buckwheat_prices')
class MinimumBuckweatPricesResource(Resource):
    def get(self):
        response_object = {'products': []}

        for product in get_buckwheat_products()[:3]:
            response_object['products'].append(get_product_data(product))

        return jsonify(response_object)


@api_rest.route('/buckwheat_products')
class BuckweatProductsResource(Resource):
    def get(self):
        response_object = {'products': []}

        for product in get_buckwheat_products():
            response_object['products'].append(get_product_data(product))

        return jsonify(response_object)


@api_rest.route('/search_products/<string:keyword>')
class SearchProductsResource(Resource):
    def get(self, keyword):
        response_object = {'products': []}

        for product in Product.objects(Q(name__icontains=keyword)):
            response_object['products'].append(get_product_data(product))

        return jsonify(response_object)
