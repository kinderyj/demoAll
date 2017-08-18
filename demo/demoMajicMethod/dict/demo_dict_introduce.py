#coding:utf-8

class Base(object):
    a = '1'
    def f1(self):
        return "f1"

ins = Base()
print ins.__dict__  #实例的__dict__是空字典，因为ins上还没有增加任何属性，有效属性a和f1都是类Base的
print Base.__dict__ #类Base的__dict__包含a和f1，以及'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Base' objects>, '__weakref__': <attribute '__weakref__' of 'Base' objects>, '__doc__': None}
print type(Base)    #<type 'type'>,类也是实例，类是type的实例
print type(Base.__dict__.get('__dict__')) #<type 'getset_descriptor'>
print dir(Base)
print type(Base.__dict__) #<type 'dictproxy'>, 还是个字典，有__dict__ 这个key
print dir(Base.__dict__.get('__dict__')) 