from flask import Blueprint
from decorators.token_required import token_required
from util.utils import response

class Test():
    base = Blueprint('class_test', __name__)

    def __init__(self):
        self.base.add_url_rule('', view_func=self.primer, methods=["GET"])
        self.base.add_url_rule('/<number>', view_func=self.segundo, methods=["GET"])

    @token_required
    def primer(self):

        send_response = {
            "message": "Estas en el test"
        }

        return response("OK", send_response)

    def segundo(self, number):

        send_response = {
            "message": f"El numero de digitaste es {number}"
        }

        return response("OK", send_response)

test = Test()