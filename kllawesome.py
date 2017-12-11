# imports from third party packages
from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict

# imports from inside project
from model import Config, Keyboard, Category

# config options
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


def to_json(record, *args, **kwargs):
    return jsonify(model_to_dict(record, *args, **kwargs))


@app.route('/')
def index():
    return jsonify({'hi': 'hello'})


@app.route('/keyboard/')
def list_keyboards():
    query = Keyboard.select()  # select all configs w/o pagination for now
    records = list(map(model_to_dict, query))

    return jsonify(records)


@app.route('/keyboard/<int:keyboard_id>')
def keyboard(keyboard_id):
    if request.method == 'GET':
        record = Keyboard.get(Keyboard.id == keyboard_id)

        return to_json(record)


@app.route('/config/', methods=['GET', 'POST'])
def list_config():
    if request.method == 'GET':
        query = Config.select()  # select all the configs for now
        records = list(map(model_to_dict, query))

        return jsonify(records)

    if request.method == 'POST':
        # lazily create without doing any input sanitation
        record = Config.create(
            name=request.form['name'],
            description=request.form['description'],
            url=request.form['url'],
            author='TODO: fill this in later',
            downloads=0,
            likes=0)

        return to_json(record)


@app.route('/config/<int:config_id>', methods=['GET', 'PUT'])
def config(config_id):
    if request.method == 'GET':
        record = Config.get(Config.id == config_id)

        return to_json(record)
