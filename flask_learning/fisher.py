import app
# from config import DEBUG
app = app.create_app()


#兼容带斜杠和不带斜杠
# 不带斜杠的url重定向到带斜杠的url上
#保证了唯一url原则，同一网页只被索引一次
#不加url不能保证用户多输入
# @app.route('/hello/')
#视图函数就是mvc中的控制器
def hello_world():
    #基于类的视图（即插视图）

    return 'Hello World!'



if __name__ == '__main__':
    #生产坏境是用nginx+uwsgi, 文件作为模块，而非入口文件，不会运行这段代码
    app.add_url_rule('/hello', view_func=hello_world) #另一种路由注册方法
    #可以自动重启服务器，详细显示异常
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81, threaded=True, processes=1) #可以在公网访问
    # app.run(host='192.168.101')

#一个cpu的核同时只能进行一个进程
#视图函数一定要返回值
#flask中请求上下文和应用上下文栈是线程隔离的
#两个上下文是被线程隔离的对象，request间接地被线程隔离
#currentapp，falsk核心对象在全局只有一个，对currentapp进行线程隔离是没有意义的，
#分离多个线程是没有意义的，因此核心对象不是线程隔离
#访问计数器不能绑定在request或者session上，只能绑定在app上，或者存储在数据库中
