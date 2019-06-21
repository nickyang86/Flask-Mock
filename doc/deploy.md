# 关于部署

### 1、使用gunicorn进行部署
参考：
https://dormousehole.readthedocs.io/en/latest/deploying/wsgi-standalone.html#gunicorn

#### 1.1 安装gunicorn
pip install gunicorn

#### 1.2 启动gunicorn
gunicorn -w 4 -b 127.0.0.1:4000 myproject:app
为了让本机之外可以访问，需要将127.0.0.1修改为0.0.0.0

