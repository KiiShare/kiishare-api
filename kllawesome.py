# imports from third party packages
from flask import Flask, request, jsonify

# imports from inside project
from model import Config

# config options
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return jsonify({'hi': 'hello'})


@app.route('/config/', methods=['GET', 'POST'])
def list_config():
    if request.method == 'GET':
        records = [rec.serialize for rec in Config.select()]

        return jsonify(records)

    if request.method == 'POST':
        # lazily create without doing any input sanitation
        record = Config.create(name=request.form['name'],
                               description=request.form['description'],
                               url=request.form['url'],

                               author='TODO: fill this in later',
                               downloads=0,
                               likes=0)

        return jsonify(record.serialize)


@app.route('/config/<int:config_id>', methods=['GET', 'PUT'])
def config(config_id):
    if request.method == 'GET':
        record = Config.get(Config.id == config_id)

        return jsonify(record.serialize)
