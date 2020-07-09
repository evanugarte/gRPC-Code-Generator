from flask import Flask
from flask import request
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
    generator = ProtoFileGenerator(proto_file, request.data)
    generator.handle_proto_generation()
    # return s3 back to user
    return 'Hello I work!'


if __name__ == '__main__':
    api.run(threaded=True)
