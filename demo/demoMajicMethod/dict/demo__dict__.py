#Adapter mode
#user only knows the f1 function, with Adapter, it can get the fInner by f1()
#The key point is the __dict__ function
class Server(object):
    def __init__(self):
        print "init Server"
    def fInner(self):
        print "f1.."

class Adapter(object):
    def __init__(self):
        print "init Adapter"
        self.__dict__.update(dict(f1=Server().fInner)) #this make the instance of Adapter has the f1
        self.__dict__.update(dict(test="this is test"))
    def f3(self):
        print "f3.."
    
    value = 1

b = Adapter()
b.f1()
print dir(b)
print b.__dict__
print Adapter.__dict__