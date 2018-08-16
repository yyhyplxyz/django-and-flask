import threading

import time


def worker():
    print("I am thread")
    time.sleep(100)
    print(threading.current_thread().getName())

new_t = threading.Thread(target=worker,name="try thread")
new_t.start()


t = threading.current_thread()
print(t.getName())
#异步编程可以充分利用多核cpu，一个核执行一段代码
#因为cpython的 GIL 全局解释器锁，同一时间程序只能运行一个线程，只能利用cpu的一个核，一定程度上保证了线程安全（在解释为bytecode后，寄存器中存储值，就变得不够安全了）
#但是对于IO密集型的程序来说，python多线程也是有意义的
