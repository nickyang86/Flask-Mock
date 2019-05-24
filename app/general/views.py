from flask import jsonify
from flask import Blueprint

bp_general = Blueprint('general', __name__)


@bp_general.route('/test')
def test():
    return jsonify('this is bp general')
