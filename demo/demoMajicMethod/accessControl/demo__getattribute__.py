#coding:utf-8


class Count(object):
    '''
            该类实现了__getattribute__方法，python invokes this method 
    for every attribute regardless whether it exists or not. 
    So that you can prevent access to attributes and make them more secure.
    '''
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax
        self.current='123'

    def __getattribute__(self, item):
        if item.startswith('cur'):
            #raise AttributeError
            return None
        '''
        Important: In order to avoid infinite recursion 
        in __getattribute__ method, its implementation should 
        always call the base class method with the same name to 
        access any attributes it needs. For example: 
        object.__getattribute__(self, name) or  
        super().__getattribute__(item) and not self.__dict__[item]
        '''
        return object.__getattribute__(self,item) 
        # or you can use ---return super().__getattribute__(item)

obj1 = Count(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.current)




class Count1(object):
    '''
            该类同时实现了__getattr__ 和 __getattribute__ 方法，会首先调用__getattribute__；
    But if  __getattribute__ raises  AttributeError exception 
    then the exception will be ignored and __getattr__ method will be invoked.
    '''
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax
        self.current=None

    def __getattr__(self, item):
            self.__dict__[item]=0
            return 0

    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item)
        # or you can use ---return super().__getattribute__(item)
        # note this class subclass object

obj1 = Count1(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.current)