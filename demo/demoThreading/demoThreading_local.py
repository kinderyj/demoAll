# encoding: UTF-8
'''
对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。
'''
import threading
 
local = threading.local()
local.tname = 'main'
 
def func():
    local.tname = 'notmain'
    print local.tname
 
t1 = threading.Thread(target=func)
t1.start()
t1.join()
 
print local.tname