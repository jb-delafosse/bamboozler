from flask import jsonify
from werkzeug import Response

from bamboozler import APP
from flask_restx import Api, Resource

API = Api(APP)


@API.route("/healthz")
class BaseView(Resource):
    @staticmethod
    def get() -> Response:
        """
        Check whether service is alive.
        """
        response = jsonify({"message": "Service is up and running"})
        response.status_code = 200
        return response
