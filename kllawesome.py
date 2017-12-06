# imports from third party packages
from flask import Flask, g, jsonify

# imports from inside project
from model import database, Config

# config options
DEBUG = True
API_VERSION = 'v1'
API_PATH = '/api/' + API_VERSION

app = Flask(__name__)
app.config.from_object(__name__)


# since flask offers before and after request callbacks we can setup and tear
# down our own db connection per request
# TODO: setup db pooling
@app.before_request
def before_request():
    g.db = database
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    return 'Hello World'


@app.route(f'{API_PATH}/config/create')
def create():
    # TODO: ingest the post request data and create record from it
    record = Config.create(url="https://google.com",
                           author="alex",
                           downloads=1,
                           likes=0)

    return jsonify(record.serialize)


@app.route(f'{API_PATH}/config/')
def list():
    records = [rec.serialize for rec in Config.select()]

    return jsonify(records)
