#coding:utf-8
'''
描述符：
就是将某种特殊类型的类的实例指派给另一个类的属性(注意：这里是类属性，而不是对象属性)。
而这种特殊类型的类就是实现了__get__，__set__,__delete__的新式类(即继承object)
'''
class Descriptor(object):  
    '''
                只要实现了__get__等三种方法中一个或几个都是描述符类。
    '''
    def __get__(self,object,type):  
        '''
        __get__方法中的object就是调用描述符对象的实例,即对象demo,type就是demo的类
        
        '''
        print 'get',self,object,type  
  
    def __set__(self,object,value):  
        print 'set',self,object,value  
  
class Demo(object):  
    desc= Descriptor()  

demo=Demo()  

demo.desc #这种调用方式其实就是下面这种调用逻辑： 
          #类Demo的__dict__里有key=desc，
          #对应的value是Descriptor(),该对象实现了__get__方法
          #所以，描述符的实例必须是另外一个类的属性，而不能是另外一个对象的属性（对象的__dict__方法没有key=desc）
Demo.__dict__['desc'].__get__(demo,type(demo))

demo.desc='my descriptor'