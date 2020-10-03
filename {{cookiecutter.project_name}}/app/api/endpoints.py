from . import api
from flask import jsonify


@api.route('/', methods=['GET'])
def root():
    return jsonify({'msg': 'Congratulations! You have successfully set up the project with cookiecutter.'}), 200
