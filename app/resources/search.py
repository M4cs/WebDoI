from app.utils.search import get_output
from flask import render_template, make_response
from app import app
from flask_restful import Resource, reqparse

def search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('q')
    return parser

class Search(Resource):
    def post(self):
        parser = search_parser()
        args = parser.parse_args()
        if args.get('q'):
            output = get_output(args['q'])
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('result.html', output=str(output), query=str(args['q'])), 200, headers)