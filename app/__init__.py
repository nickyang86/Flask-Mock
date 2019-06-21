"""
 @Topic:
 @Date: 106831269@qq.com
 @Author: nick.yang
"""

from flask import Flask, jsonify
from app.helpers import select_config
from flask_cors import CORS
from flask import render_template
from app.general.views import bp_general

app = Flask(__name__, static_folder="../frontend/dist/static", template_folder="../frontend/dist")
app.config.from_object(select_config())
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

# 注册blueprint
app.register_blueprint(bp_general, url_prefix='/general')


@app.route('/')
def index():
    return render_template('index.html')


# 模拟前端登录成功
@app.route('/user/login', methods=['POST'])
def user_login():
    return jsonify(dict(code=20000, data=dict(token="admin-token")))


@app.route('/user/info', methods=['GET'])
def user_info():
    return jsonify(
        dict(
            code=20000,
            data=dict(
                roles=["admin"],
                introduction="I am a super administrator",
                avatar="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                name="Super Admin"
            )
        )
    )
