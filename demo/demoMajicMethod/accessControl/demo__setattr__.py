#coding:utf-8

class Base(object):
    '''
    __setattr__() is called whenever a value is assigned to 
    any of the class's property. Even if the property is 
    initialized in the __init__(), it will make call to __setattr__()
            和 __getattr__ 不同， __setattr__ 可以用于真正意义上的封装。它允许你自定义某个
            属性的赋值行为，不管这个属性存在与否，也就是说你可以对任意属性的任何变化都定义自己的规则。
    
    uuid模块的UUID类实现了__setattr__方法，用于限制class's property被修改:
        def __setattr__(self, name, value):
            raise TypeError('UUID objects are immutable')
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __setattr__(self, k, v):
        print 'Set Attr: {} -> {}'.format(k, v)

ins = Base(1,2)
ins.a = 10


