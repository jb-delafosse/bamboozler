from . import app
from flask import request

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/trello/event', methods=['GET'])
def handle_trello_request():
    return 'Handle trello request here'
