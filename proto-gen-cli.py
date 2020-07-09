from tools.colors import Colors
from argparse import ArgumentParser
import os
import requests

parser = ArgumentParser()

parser.add_argument(
    'proto_path', nargs=1,
    help='The path to the proto file to generate code for.')
parser.add_argument(
    '--language', nargs='+',
    help='The language(s) to generate proto code.')

args = parser.parse_args()


class ProtoGeneratorClient:
    SERVER_URL = 'http://127.0.0.1:5000/'
    colors = Colors()
    language_map = {
        'js': True,
        'py': True
    }

    def __init__(self, proto_path, language_types):
        self.proto_path = proto_path
        self.full_proto_path = os.path.join(os.getcwd(), proto_path)
        self.language_types = language_types

    def check_file_path(self):
        self.colors.print_purple('Checking file path...')
        if not os.path.isfile(self.full_proto_path):
            raise FileNotFoundError(
                f'The path {self.proto_path} could not be resolved.')
        self.colors.print_green('File found!')

    def check_language_types(self):
        self.colors.print_purple('Checking supplied language type...')
        for language in self.language_types:
            if language not in self.language_map:
                self.print_supported_languages(language)
        self.colors.print_green('The given languages are supported!')

    def check_server_health(self):
        self.colors.print_purple('Checking if server is up...')
        healthy = False
        try:
            requests.get(self.SERVER_URL)
            self.colors.print_green(f'The server is up!')
        except requests.exceptions.ConnectionError:
            self.colors.print_red(f'The server at {self.SERVER_URL} is down.')
        return healthy

    def call_generate_api(self):
        pass

    def handle_proto_generation(self):
        self.colors.print_blue('Welcome to the gRPC proto code generator!')
        self.check_file_path()
        self.check_language_types()
        if self.check_server_health():
            self.call_generate_api()

    def print_supported_languages(self, unsupported_type):
        supported_types = ', '.join(
            [type for type in self.language_map.keys()])
        error_str = f'Sorry! \'{unsupported_type}\' is not a supported language\
 type. Supported types are: {supported_types}'
        raise NotImplementedError(error_str)


if __name__ == "__main__":
    generator = ProtoGeneratorClient(args.proto_path[0], args.language)
    generator.handle_proto_generation()
