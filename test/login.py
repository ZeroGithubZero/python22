from flask import Flask


# 1.创建项目配置类
class Config(object):
    # 配置信息以类的属性方法定义即可
    # 1.当代码修改后能自动重启项目，2.服务器代码报错的时候回错误定位
    DEBUG = True
    # mysql连接配置..
    pass


# 2.创建app对象
app = Flask(__name__)


# 3.将配置类中的配置读取到app项目中
app.config.from_object(Config)

# app.config.from_pyfile("config.ini")
# app.config.from_envvar("FLASKCONFIG")

"""
端口被占用：杀死进程号
lsof -i:5000
kill -9 进程号

一条命令搞定：kill -9 $(lsof -i:5000)
"""


# 将路由和视图函数绑定到一起
@app.route('/')
def index():
    a = 1/0
    return "index 666"

# 运行项目
if __name__ == '__main__':
    app.run()