from flask import Flask

api = Flask(__name__)


@api.route('/', methods=['GET'])
def get_companies():
    return 'Hello I work!'


if __name__ == '__main__':
    api.run()
