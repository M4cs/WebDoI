from flask import Flask, jsonify, render_template, send_file
from flask_restful import Api
from app.utils.helpers import api_response
from app.utils.search import get_output
app = Flask(__name__)
api = Api(app)

@app.route('/api')
def index():
    return api_response('WebDoI API Root', 200)

@app.route('/')
def home():
    return render_template('index.html')

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

from app.resources.search import Search

api.add_resource(Search, '/api/search')