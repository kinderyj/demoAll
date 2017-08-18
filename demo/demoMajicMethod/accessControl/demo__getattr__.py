#coding:utf-8

class CountWithout__getattr__():
    '''
            该类没有__getattr__方法，调用不存在的属性时，会报AttributeError
    '''
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax

obj1 = CountWithout__getattr__(1,10)
print(obj1.mymin)
print(obj1.mymax)
#print(obj1.mycurrent)  #--> AttributeError: 'Count' object has no attribute 'mycurrent'

class CountWith__getattr__(object):
    '''
            该类实现了__getattr__方法，调用不存在的属性时，不会报AttributeError，会得到
    __getattr__方法的返回值;
    Python will call  __getattr__ method whenever you 
    request an attribute that hasn't already been defined.
    '''
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax

    def __getattr__(self, item):
        self.__dict__[item] = 'the attr %s does not exist, this message is the attr' % item
        '''
                        这里需要return object.__getattribute__(self,item)，
                        否则对实例执行dir()方法会提示none type is not callable；
                        而且当前类需要继承object，也就是新式类；
        '''
        return object.__getattribute__(self,item) 
    
obj1 = CountWith__getattr__(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.mycurrent) 
print dir(obj1)


print dir(object)
