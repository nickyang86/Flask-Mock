"""
 @Topic:
 @Date: 106831269@qq.com
 @Author: nick.yang
"""

from flask import Flask, jsonify
from app.helpers import select_config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(select_config())
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

from app.general.views import bp_general

app.register_blueprint(bp_general, url_prefix='/general')


@app.route('/user/login', methods=['POST'])
def login():
    return jsonify(dict(code=20000, data=dict(token="admin-token")))
