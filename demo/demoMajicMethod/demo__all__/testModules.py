#coding: utf-8
'''
当使用from testModules import * 的时候，默认会导出所有的不以下划线开头的
变量，方法，和类；
当使用了__all__,会重写以上默认行为，只导出__all__指定的变量，方法和类。
'''

__all__ = ['_B']
class A(object):
    def fa(self):
        pass

class _B(object):
    def fb(self):
        pass

def f2():
    pass

def _f3():
    pass

a = 1
__b = 2