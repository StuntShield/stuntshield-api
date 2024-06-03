from flask import Blueprint

from .controllers.StuntingController import StuntingController

blueprint = Blueprint('blueprint', __name__)


# define the routes
blueprint.route('/', methods=['GET'])(StuntingController.index)
# blueprint.route("/stunting-classification", methods=["GET"])(index)
# blueprint.route("/create", methods=["GET"])(create)
# blueprint.route("/insert", methods=["GET"])(insert)
