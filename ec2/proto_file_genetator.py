import os
from os import path
import uuid
import shutil
import time


class ProtoFileGenerator():
    proto_file = None
    uuid_directory = None

    def __init__(self, proto_file, language_types):
        self.proto_file = proto_file
        self.uuid_directory = str(uuid.uuid4())
        self.original_directory = os.getcwd()

    def save_proto_file(self):
        self.proto_file.save(path.join(os.getcwd(), self.proto_file.filename))

    def generate_node_files(self):
        os.system(f'protoc-gen-grpc \
            --js_out=import_style=commonjs,binary:./ \
            --grpc_out=./ --proto_path ./ \
            ./{self.proto_file.filename}')

    def generate_python_files(self):
        os.system(f'python3 -m grpc_tools.protoc -I. --python_out=./ \
            --grpc_python_out=./ {self.proto_file.filename}')

    def create_uuid_directory(self):
        os.mkdir(self.uuid_directory)
        os.chdir(self.uuid_directory)
        self.save_proto_file()

    def remove_uuid_directory(self):
        os.chdir(self.original_directory)
        time.sleep(5)
        shutil.rmtree(self.uuid_directory, ignore_errors=True)

    def handle_s3_upload(self):
        pass

    def handle_proto_generation(self):
        self.create_uuid_directory()
        self.generate_node_files()
        self.generate_python_files()
        # upload files to s3
        # grab the links
        self.remove_uuid_directory()
        # return the links to the user
