# Flask

### 1、指定static及templates目录
```.python
app = Flask(__name__, static_folder="../frontend/dist/static", template_folder="../frontend/dist")
```
在实例化Flask的时候，指定static_folder与template_folder，这样调用render_template()的时候不会找不到html及相关资源文件。

### 2、 定义入口页面
```.python
@app.route('/')
def index():
    return render_template('index.html')
```

### 3、前后端分离式开发，解决跨越问题
```.python
from flask_cors import CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})
```
在frontend/src/utils/request.js中修改 baseURL，使用后端服务器的ip及端口 "http://127.0.0.1:5000/"

### 4、使用blueprint
blueprint可以更加结构化的组织代码，将同一类型的通过名字进行区别
#### 4.1 实例化
```.python
from flask import Blueprint

bp_general = Blueprint('general', __name__)
```
#### 4.2 装饰视图函数
```.python
@bp_general.route('/test')
def test():
    return jsonify(dict(code=20000, message='this is bp general'))
```
使用@bp_general.route()对视图函数进行装饰，与Flask.route类似，第一个参数是url规则，还可以接受其他参数，如限定请求方法的methods
#### 4.3 注册
```.python
from app.general.views import bp_general
app.register_blueprint(bp_general, url_prefix='/general')
```
在flask的实例app上对bp_general进行注册，url_prefix='/general'表示所有/general请求都将指向bp_general装饰的视图函数
