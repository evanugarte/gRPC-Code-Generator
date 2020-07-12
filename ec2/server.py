from flask import Flask
from flask import request
from flask import jsonify
import uuid
import os
from proto_file_genetator import ProtoFileGenerator

api = Flask(__name__)


@api.route('/', methods=['GET'])
def handle_health_check():
    return 'Hello I work!'


@api.route('/generate', methods=['POST'])
def generate_grpc_code():
    file_name = list(request.files.keys())[0]
    proto_file = request.files[file_name]
    generator = ProtoFileGenerator(proto_file, request.args)
    return jsonify(generator.handle_proto_generation())


if __name__ == '__main__':
    api.run(threaded=True)
