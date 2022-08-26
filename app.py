from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import escape
from services.test import test
from util.utils import response
import jwt
from decorators.token_required import token_required, secret_key, get_time_exp

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret_key_bmfl'

class Main:

    def __init__(self):
        app.add_url_rule('/login', view_func=self.login, methods=['POST'])
        app.add_url_rule('/user/<username>', view_func=self.show_user_profile, methods=['GET', 'POST'])

    def login(self):
        print("sdasd")
        #auth = request.authorization
        username = request.json['username']
        password = request.json['password']

        data = {
            "id_user": 1,
            "username" : username,
        }

        print(data)

        token = jwt.encode({'data': data, 'exp' : get_time_exp(1)}, secret_key, algorithm='HS256')

        send_response = {
            "user": data,
            "token": token
        }

        return response("OK", send_response)

    @token_required
    def show_user_profile(self, username ):
        # show the user profile for that user
        send_response = {
            "message": f"User => {username}"
        }

        return response("OK", send_response);

def register(name_class, url_prefix):
    app.register_blueprint(name_class, url_prefix=f"/{url_prefix}")

def initalize():
    Main()
    register(test.base, 'test')

initalize()
print("incio!!!")

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)