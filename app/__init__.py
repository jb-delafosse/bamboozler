from flask import Flask

app = Flask(__name__)

TECH_ACCOUNT = ''

from . import trello_task

if __name__ == "__main__":
    app.run()
