import os
from os import path
import uuid
import shutil
from s3_handler import S3Handler
import time


class ProtoFileGenerator():
    proto_file = None
    uuid_directory = None
    original_directory = None
    language_types = None
    s3_handler = None

    def __init__(self, proto_file, language_types):
        self.proto_file = proto_file
        self.uuid_directory = str(uuid.uuid4())
        self.original_directory = os.getcwd()
        self.language_types = language_types
        self.s3_handler = S3Handler()
        self.generator_dict = {
            'js': self.generate_node_files,
            'py': self.generate_python_files
        }

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
        shutil.rmtree(self.uuid_directory, ignore_errors=True)

    def handle_s3_upload(self):
        for file in os.listdir('.'):
            if not file.endswith('.proto'):
                self.s3_handler.upload_file(file, self.uuid_directory)
        return self.s3_handler.get_file_urls(self.uuid_directory)

    def generate_specified_language_code(self):
        for language_type in self.language_types.keys():
            if language_type in self.generator_dict:
                self.generator_dict[language_type]()

    def handle_proto_generation(self):
        self.create_uuid_directory()
        self.generate_specified_language_code()
        files = self.handle_s3_upload()
        self.remove_uuid_directory()
        return files
