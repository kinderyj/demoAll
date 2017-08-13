#coding:utf-8
'''
未使用锁，多个线程同时操作一个内存中的资源，运行结果会产生混乱
'''
import threading
import time

class withoutLock(object):
    def __init__(self):
        self.gl_num = 0

    def show(self,arg):
        global gl_num
        time.sleep(1)
        self.gl_num +=1
        print self.gl_num
    def f_exec(self):
        for i in range(10):
            t = threading.Thread(target=self.show, args=(i,))
            t.start()
        print 'main thread stop'

class withLock(object):
    '''
            全局变量在在每次被调用时都要获得锁，才能操作，因此保证了共享数据的安全性
    '''
    def __init__(self):
        self.gl_num = 0
        self.lock = threading.RLock()

    def show(self,arg):
        self.lock.acquire()
        global gl_num
        self.gl_num +=1
        time.sleep(1)
        print self.gl_num
        self.lock.release()
    def f_exec(self):
        for i in range(10):
            t = threading.Thread(target=self.show, args=(i,))
            t.start()
        print 'main thread stop'
#withoutLock().f_exec()
withLock().f_exec()
