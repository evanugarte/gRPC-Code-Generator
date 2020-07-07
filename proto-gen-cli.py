from tools.colors import Colors
from argparse import ArgumentParser
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
    colors = Colors()
    language_map = {
        'js': True,
        'py': True
    }

    def __init__(self, proto_path, language_types):
        self.colors.print_blue('Welcome to the gRPC proto code generator!')
        self.colors.print_purple('Checking file path...')
        self.proto_path = os.path.join(os.getcwd(), proto_path)
        if not os.path.isfile(self.proto_path):
            raise FileNotFoundError(f'The path {proto_path} could not be resolved.')
        self.colors.print_green('File found!')
        self.colors.print_purple('Checking supplied language type...')
        for language in language_types:
            if language not in self.language_map:
                self.print_supported_languages(language)
        self.colors.print_green('The given languages are supported!')

    def print_supported_languages(self, unsupported_type):
        supported_types = ', '.join(
            [type for type in self.language_map.keys()])
        error_str = f'Sorry! \'{unsupported_type}\' is not a supported language\
 type. Supported types are: {supported_types}'
        raise NotImplementedError(error_str)


if __name__ == "__main__":
    generator = ProtoFileGenerator(args.proto_path[0], args.language)
