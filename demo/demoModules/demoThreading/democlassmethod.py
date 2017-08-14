class Base(object):
    def __init__(self):
        self.ret={}
        self.ret['code'] = 0
        self.ret['data'] = {}
    
    @classmethod
    def checker(cls, fun):
        def inner(cls1, flag):
            cls1.ret = dict(code=0,data={})  
            return fun(cls1, flag)
        return inner

class A(Base):
    def __init__(self):
        super(A,self).__init__()
    
    @Base.checker    
    def fa(self, flag):
        if flag:
            self.ret['a'] = 1  
        print self.ret


a=A()
a.fa(True)
a.fa(False)
a.fa(True)