# coding: utf-8

class Base(object):
    '''
    *args:位置参数
    **kwargs:命名参数
    '''
    def __init__(self,*args,**kwargs):
        print type(args), args
        print type(kwargs), kwargs

s = 'a'
t = (1,2,3)
d = {'x':1,'v':2}

#'a','b','c', t, d都是位置参数，都传递给了*args
Base(s, t, d) #打印<type 'tuple'> ('a', (1, 2, 3), {'x': 1, 'v': 2}) <type 'dict'> {}
#传递元祖t的时候，加上*，表示对这个元祖进行解析，传递元祖里面的每个元素给*args
Base(s,t,*t) #打印<type 'tuple'> ('a', (1, 2, 3), 1, 2, 3) <type 'dict'> {}
#传递字典d的时候，加上*，表示解析出字典的key，并作为位置参数传递给*args
Base(s,t,*d) #打印<type 'tuple'> ('a', (1, 2, 3)) <type 'dict'> {'x': 1, 'v': 2}
#传递字典d的时候，加上**，表示解析出字典的key：value 这个map，并传递给**kwargs
Base(s,t,**d)