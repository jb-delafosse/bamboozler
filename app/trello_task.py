from . import app
from flask import request

@app.route('/', methods=['GET'])
def handle_trello_event():
    return 'Hello, World!'
