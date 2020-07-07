from tools.colors import Colors
from argparse import ArgumentParser
from argparse import HelpFormatter
import os

parser = ArgumentParser()

parser.add_argument(
    'proto_path', nargs=1,
    help='The path to the proto file to generate code for.')
parser.add_argument(
    '--language', nargs='+',
    help='The language(s) to generate proto code.')

args = parser.parse_args()


class ProtoFileGenerator:
    c = Colors()
    language_map = {
        'js': True,
        'py': True
    }

    def __init__(self, proto_path, language_types):
        self.proto_path = os.path.join(os.getcwd(), proto_path)
        self.c.print_yellow(os.path.isfile(self.proto_path))
        self.c.print_yellow(self.proto_path)
        if not os.path.isfile(self.proto_path):
            raise FileNotFoundError('The given file doesn\'t exist!')
        for language in language_types:
            if language not in self.language_map:
                self.print_supported_languages(language)
        pass

    def print_supported_languages(self, unsupported_type):
        supported_types = ', '.join(
            [type for type in self.language_map.keys()])
        error_str = f'Sorry! \'{unsupported_type}\' is not a supported language\
type. Supported types are: {supported_types}'
        raise NotImplementedError(error_str)

    def check_ec2_connection(self):
        # wait for response
        # else print red that we cant
        pass

    def handle_proto_generation(self):
        # attempt multipart upload
        pass


if __name__ == "__main__":
    generator = ProtoFileGenerator(args.proto_path[0], args.language)
    
