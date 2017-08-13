# coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s\r' % threading.currentThread().getName()
    print 'the arg is:%s\r' %arg
    time.sleep(1)

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    '''
            设置setDaemon为false，主线程执行过程中，前台线程也在进行，
            主线程执行完毕后，等待前台线程也执行完成后，主线程停止。
            默认就为False，可以不用显示的声明
    '''
    t.setDaemon(False)
    t.start()

print 'main_thread end!'

