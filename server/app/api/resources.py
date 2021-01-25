"""
REST API Resource Routing
"""

import os

from datetime import datetime
from flask import request, jsonify, send_from_directory
from flask_restplus import Resource

from .security import require_auth
from . import api_rest

from mongoengine import connect, Q
from ..db_models.shop import Shop
from ..db_models.product import Product
from ..config import Config

connect(Config.DB_NAME, alias='default')


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
            'img_link': request.url_root + 'api/product-img/{product_id}'.format(product_id=product.id),
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


@api_rest.route('/product-img/<string:product_id>')
class SearchProductsResource(Resource):
    def get(self, product_id):
        current_proj_dir = os.path.dirname(os.path.realpath(__file__)) + '/..'
        result_img_path = current_proj_dir + '/static/imgs/no_img.jpg'

        product = Product.objects(id=product_id).first()
        if product and product.img_path:
            result_img_path = current_proj_dir + product.img_path

        dir_path = '/'.join(result_img_path.split('/')[:-1])
        file_name = result_img_path.split('/')[-1]

        return send_from_directory(dir_path, file_name)
