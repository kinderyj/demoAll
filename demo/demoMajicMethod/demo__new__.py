#coding: utf-8
'''
__new__ 用于创建类的实例，作用于__init__方法之前
'''

# -*- coding: utf-8 -*-
 
class Person(object):
    '''
            该类的打印输出可以说明，__new__ 在__init__之前执行，创建一个实例并返回
    '''
    def __new__(cls, name, age):
        print '__new__ called.'
        return super(Person, cls).__new__(cls, name, age)
 
    def __init__(self, name, age):
        print '__init__ called.'
        self.name = name
        self.age = age
 
    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

class PositiveInteger_incorrect(int):
    '''
            通过该类试图：继承int类，重载__init__方法，只生产正整数，但是
    int，str，tuple这种不可变的类，是无法通过__init__
            进行重载的
    '''
    def __init__(self, value):
        super(PositiveInteger_incorrect, self).__init__(self, abs(value))
        
class PositiveInteger_correct(int):
    '''
            对于int，str，tuple这种不可变的类，需要通过重载__new__
            进行改写
    '''
    def __new__(cls, *args, **kwargs):
        return super(PositiveInteger_correct, cls).__new__(cls, abs(*args)) 

 
if __name__ == '__main__':
    p = Person('kin', 24)
    print p
    
    i = PositiveInteger_incorrect(-3)
    print i
    
    i = PositiveInteger_correct(-3)
    print i