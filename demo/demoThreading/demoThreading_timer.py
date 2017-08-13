# encoding: UTF-8
import threading


def func():
    print 'hello timer!'

'''
Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。
构造方法： 
Timer(interval, function, args=[], kwargs={}) 
　　interval: 指定的时间 
　　function: 要执行的方法 
　　args/kwargs: 方法的参数
'''
timer = threading.Timer(5, func)
timer.start()