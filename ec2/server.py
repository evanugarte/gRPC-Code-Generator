from flask import Flask
import uuid
import os

api = Flask(__name__)


@api.route('/', methods=['GET'])
def handle_health_check():
    return 'Hello I work!'


@api.route('/generate', methods=['POST'])
def generate_grpc_code():
    return 'Hello I work!'


if __name__ == '__main__':
    api.run()
