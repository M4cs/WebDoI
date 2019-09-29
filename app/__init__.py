from flask import Flask, jsonify, render_template, send_file, make_response
from flask_restful import Api, reqparse
from app.utils.helpers import api_response
from app.utils.search import get_output
import json

app = Flask(__name__)
api = Api(app)

def search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('query')
    return parser

@app.route('/')
def index():
    parser = search_parser()
    args = parser.parse_args()
    if args.get('query'):
        output = get_output(args['query'])
        headers = {'Content-Type': 'text/html'}
        with open('app/db/count.json', 'r+') as json_in:
            json_obj = json.load(json_in)
            count = json_obj['count']
            count += 1
            json_obj['count'] = count
            json_in.seek(0)
            json_in.truncate()
            json.dump(json_obj, json_in, indent=4)
            json_in.close()
        return make_response(render_template('result.html', output=str(output), query=str(args['query'])), 200, headers)
    else:
        with open('app/db/count.json', 'r+') as json_in:
            json_obj = json.load(json_in)
            count = json_obj['count']
            json_in.close()
        return render_template('index.html', count=count)

@app.route('/assets/css/<css>')
def css(css):
    return send_file('templates/assets/css/{}'.format(css))

@app.route('/assets/js/<js>')
def js(js):
    return send_file('templates/assets/js/{}'.format(js))

@app.route('/api/assets/css/<css>')
def css_api(css):
    return send_file('templates/assets/css/{}'.format(css))

@app.route('/api/assets/js/<js>')
def js_api(js):
    return send_file('templates/assets/js/{}'.format(js))

@app.route('/about')
def about():
    return render_template('about.html')

from app.api_search import  SearchAPI

api.add_resource(SearchAPI, '/api/search')