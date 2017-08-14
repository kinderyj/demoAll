# -*- coding: utf-8 -*-
'''
http://www.cnblogs.com/tkqasn/p/5700281.html
threading用于提供线程相关的操作，线程是应用程序中工作的最小单元。
python当前版本的多线程库没有实现优先级、线程组，线程也不能被停止、暂停、恢复、中断。

threading模块提供的类：  
　　Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local。

threading 模块提供的常用方法： 
　　threading.currentThread(): 返回当前的线程变量。 
　　threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
　　threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

threading 模块提供的常量：

threading.TIMEOUT_MAX 设置threading全局超时时间。
'''