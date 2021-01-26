from flask_restplus import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('keyword',
                    type=str,
                    required=True)
