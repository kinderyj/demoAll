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
            主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程均停止。
    '''
    t.setDaemon(True)
    t.start()

print 'main_thread end!'

