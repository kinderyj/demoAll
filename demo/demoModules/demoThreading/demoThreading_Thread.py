# coding:utf-8
'''
Thread是线程类，有两种使用方法，直接传入要运行的方法或从Thread继承并覆盖run()
'''
import threading
import time
#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    time.sleep(1)
    print 'the arg is:%s and the current thread name is %s\r' % (
        arg,threading.currentThread().getName())

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print 'main thread end!'

#方法二：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        print 'the arg in MyThread is:%s\r' % self.arg

for i in xrange(4):
    t =MyThread(i)
    t.start()

print 'main thread end!'