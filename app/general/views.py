from flask import jsonify
from flask import Blueprint

bp_general = Blueprint('general', __name__)


@bp_general.route('/test', methos=[])
def test():
    return jsonify(dict(code=20000, message='this is bp general'))
