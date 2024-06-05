from flask import Blueprint

from .controllers.LLMController import getPrompt

blueprint = Blueprint('blueprint', __name__)


# define the routes
# blueprint.route('/', methods=['GET'])(StuntingController.index)
blueprint.route('/prompt', methods=['GET'])(getPrompt)
# blueprint.route("/stunting-classification", methods=["GET"])(index)
# blueprint.route("/create", methods=["GET"])(create)
# blueprint.route("/insert", methods=["GET"])(insert)
