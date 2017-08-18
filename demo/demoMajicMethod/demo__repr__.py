# coding: utf-8
'''
__repr__也是将对象序列化，但是__repr__更多的是给python编译器看的。__str__更多的是可读性(readable)。
我们将repr()函数作用于摸某一个对象的时候，调用的其实就是该函数的__repr__函数。
与repr()成对的是eval()函数。eval()函数是将序列化后的对象重新转为对象。前提是该对象实现了__repr__函数
例1：
uuid模块的UUID类实现了__repr__方法；
    def __repr__(self):
        return 'UUID(%r)' % str(self)
'''

class Fraction:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __str__(self):
        return '(' + str(self.__num) + '/' + str(self.__den) + ')'
    
    def __repr__(self):
        return 'Fraction (' + str(self.__num) + ',' + str(self.__den) + ')'
    
    def f1(self):
        print self.__num, self.__den

f = Fraction(1,2)
print str(f) #调用__str__方法
print repr(f) #调用__repr__方法
print type(eval(repr(f))) #repr 和 eval是成对的，即：eval将repr计算过的值，重新转换成实例
eval(repr(f)).f1() #eval将repr计算过的值，重新转换成实例，于是有了f1方法