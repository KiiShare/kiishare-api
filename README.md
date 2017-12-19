# kiishare-api
Backend  to support keyboard config sharing service

## Setup

1. create tables `pipenv run python -c 'import model; model.setup_db()`

## Running

Since we are using flask we just use the default way to launch a flask app:

`FLASK_APP=kllawesome.py flask run`

or in the dev envrionment with `pipenv`

`FLASK_APP=kllawesome.py FLASK_DEBUG=1 pipenv run flask run`
