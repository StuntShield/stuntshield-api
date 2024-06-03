from flask import jsonify


class StuntingController:

    # get all data
    def index():

        return jsonify({"data": "hello", "message": "woooss!"})

    # show specific user
    def show():
        pass
