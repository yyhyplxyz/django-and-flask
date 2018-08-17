import threading

import time


# def worker():
#     print("I am thread")
#     time.sleep(100)
#     print(threading.current_thread().getName())
#
# new_t = threading.Thread(target=worker,name="try thread")
# new_t.start()


t = threading.current_thread()
print(t.getName())
#异步编程可以充分利用多核cpu，一个核执行一段代码
#因为cpython的 GIL 全局解释器锁，同一时间程序只能运行一个线程，只能利用cpu的一个核，一定程度上保证了线程安全（在解释为bytecode后，寄存器中存储值，就变得不够安全了）
#但是对于IO密集型的程序来说，python多线程也是有意义的
#flask默认是单进程单线程, 可以在app中设置多个线程或进程来处理访问请求，可是当有多个请求时，服务器实例化多个request对象，无法确定哪个对象针对哪个用户的请求
#需要使用线程隔离 利用线程id号作为字典分隔, 如下两个线程中的Try是两个不同的实例

from werkzeug.local import Local, LocalStack
#
# Try = Local()
# Try.b = 1
#
# def learn_local():
#     Try.b = 2
#     print("in a new threa" + str(Try.b))
#
# new_thread = threading.Thread(target=learn_local)
# new_thread.start()
#
# print("In main thread" + str(Try.b))

# s = LocalStack()
# s.push(1)
# print(s.top)
# print(s.top)
# s.pop()
# print(s.top)

my_stack = LocalStack()
my_stack.push(1)
print("In main thread after push " + str(my_stack.top))

def learn_local_stack():
    print("In new thread before push " + str(my_stack.top))
    my_stack.push(2)
    print("In new thread before push " + str(my_stack.top))

new_t = threading.Thread(target=learn_local_stack)
new_t.start()

time.sleep(1)
print("finally in main thread " + str(my_stack.top))

#使用线程隔离的意义是使当前线程能够正确引用到他自己创建的对象
#而不是其他线程创建的对象


