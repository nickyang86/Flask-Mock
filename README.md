# Flask-Mock
使用Flask开发一个Mock项目，采用前后端分离的方式，不使用flask本身的模板。
Flask文档路径：http://flask.pocoo.org/docs/1.0/

### 一、在github上新建仓库，并clone到本地
```
git clone https://github.com/nickyang86/Flask-Mock.git
```

### 二、引入前端开源项目
> 使用前后端分离的模式进行开发，前端使用开源的[vue-element-admin](https://github.com/PanJiaChen/vue-element-admin)项目，
后端使用Flask
- 在项目根目录中clone vue-element-admin项目
```
git clone https://github.com/PanJiaChen/vue-element-admin
```
- 将vue-element-admin目录名称修改为frontend

### 三、创建虚拟环境
- 使用pipenv创建虚拟环境，基于python3.7
```
pipenv --three
```
- 在pycharm中将新生成的虚拟环境配置到项目解释器中，重新打开一个终端后，pycharm会自动进入到pipenv shell中

### 四、创建项目目录
- 在项目根目录中增加一个python包，命名为app，Flask所有相关都将存放在此包中
- 在项目根目录中增加两个文件，.env及.flaskenv，这两个文件需要配合python-dotenv使用，其中.env
保存一些敏感配置，不可以同步到github上，.flaskenv保存一些开放配置

### 五、安装Flask及其他库
- pipenv install flask
- pipenv install flask-sqlalchemy
- pipenv install python-dotenv
- ...

### 六、安装前端依赖库并允许
- 进入frontend目录，执行npm install
- 执行npm run dev 运行开发模式

### 七、本地运行后端调试
flask run，默认端口为5000
指定端口运行： flask run -p 5002
flask run 会自动搜索app下的Flask实例。

### 八、Flask配置
- 全局配置FLASK_ENV: export FLASK_ENV=development
- 通过dotenv配置
- .env文件保存一些非公开的配置
- .flaskenv保存一些公开配置

