import os
import uuid


class ProtoFileGenerator():
    proto_file = None
    uuid_directory = None

    def __init__(self, proto_file, language_types):
        self.proto_file = proto_file
        self.uuid_directory = str(uuid.uuid4())
        self.original_directory = os.getcwd()

    def save_proto_file(self):
        pass

    def generate_node_files(self):
        pass

    def generate_python_files(self):
        pass

    def create_uuid_directory(self):
        os.mkdir(self.uuid_directory)
        os.chdir(self.uuid_directory)
        self.save_proto_file()

    def remove_uuid_directory(self):
        os.chdir(self.original_directory)
        os.rmdir(self.uuid_directory)

    def handle_s3_upload(self):
        pass

    def handle_proto_generation(self):
        self.create_uuid_directory()
        # create uuid/.proto
        # cd in the directory
        # if js do js
        # if py do py
        # upload files to s3
        self.remove_uuid_directory()
