#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://hackerxu.com/2014/10/09/subprocess.html
import subprocess

def subprocess_Popen():
    '''
            无阻塞,会和主程序并行运行
    '''
    subprocess.Popen(["python","datas.py"])

def subprocess_call():
    '''
            阻塞，主程序必须等待命令执行完毕
    '''
    subprocess.call(["python","datas.py"])

def subprocess_Popen_withWait():
    '''
            加上wait方法，变成阻塞方式,主程序必须等待命令执行完毕
    '''
    s = subprocess.Popen(["python","datas.py"])
    s.wait()

def subprocess_Popen_withRetData_v1():
    '''
            获取子进程的返回值：在初始化Popen的时候，设置stdout=subprocess.PIPE，
            然后调用communicate() 
    '''
    s = subprocess.Popen(["python","datas.py"],stdout=subprocess.PIPE)
    return s.communicate() 

def subprocess_Popen_withRetData_v2():
    '''
            获取子进程的返回值：还有一种更简单的方式(v1可以实现更多的交互,如stderr和stdin)：
            subprocess.check_output(["python","datas.py"])
    '''
    s = subprocess.check_output(["python","datas.py"])
    return s

def subprocess_Popen_input():
    '''
            给子进程输入，以下过程为，先打开一个python执行环境，然后输入python代码：import datas
    '''
    s = subprocess.Popen(["python"],stdin=subprocess.PIPE)
    return s.communicate("import datas")

subprocess_Popen_input()