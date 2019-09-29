from flask_restful import Resource, reqparse
from app.utils.search import get_output

def search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('q', help='Query Search', required=True)
    return parser

class SearchAPI(Resource):
    def get(self):
        parser = search_parser()
        args = parser.parse_args()
        output = get_output(args['q'])
        return { 'answer': output }, 200