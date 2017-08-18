#coding:utf-8

class DemoProperty(object):
    '''
    property是python内置的装饰器方法，
            注意：
        1.使用property的类一定是新式类，即继承自object的类。
        2.如果类中只使用了@property，就是将被修饰的方法定义为只读的属性
                                  尝试赋值的时候会提示触发异常：
                dP.pro = 3
                AttributeError: can't set attribute
                    
    '''
    def __init__(self):
        self._x = 1
    
    @property    
    def pro(self):
        return self._x
    
    @pro.setter
    def pro(self,value):
        if not isinstance(value, int):
            raise ValueError('should be int')
        if value < 0:
            raise ValueError('shoud > 0')
        self._x = value
    
    @pro.deleter
    def pro(self):
        del self._x


dP = DemoProperty()
print dP.pro  #1
dP.pro = 3
print dP.pro  #3
del dP.pro
#print dP.pro() #AttributeError: 'DemoProperty' object has no attribute '_x'