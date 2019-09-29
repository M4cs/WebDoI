from flask_restful import Resource, reqparse
from app.utils.search import get_output

def search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('q', help='Query Search', required=True)
    parser.add_argument('n')
    parser.add_argument('a')
    parser.add_argument('l')
    return parser

class SearchAPI(Resource):
    def get(self):
        parser = search_parser()
        args = parser.parse_args()
        query = args['q']
        if args['n']:
            query += ' ' + '-n' + args['n']
        if args['a']:
            query += ' ' + '-a'
        if args['l']:
            query += ' ' + '-l'
        output = get_output(args['q'])
        return { 'answer': output }, 200