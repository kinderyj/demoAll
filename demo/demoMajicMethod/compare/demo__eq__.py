class DemoEq(str):
    '''
    Python中有个比较操作符==用来比较两个变量的大小，而这个操作符
            是通过内置函数__eq__来实现的，所以我们只需要通过改变这个内置函数代码，
            就可以改变重新定义这个操作符的行为;
            注意：需要继承str类
    '''
    def __eq__(self, other):
        return len(self) == len(other)

d1 = DemoEq('abc')
d2 = DemoEq('avv')
print d1==d2
print 'abc' == 'avv'