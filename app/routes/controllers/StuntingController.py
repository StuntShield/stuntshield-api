from flask import jsonify
from flask import request


class StuntingController:

    # get all data
    def index():

        # get request parameter
        username = request.args.get('username')
        password = request.args.get('password')

        return jsonify(
            {'data_test': {'username': username, 'password': password}}
        )

    # show specific user
    def show():
        pass
