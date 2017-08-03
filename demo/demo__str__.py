
class Base(object):
    def __init__(self):
        print 'init'
    def f1(self):
        print 'f1'

print Base() #<__main__.Base object at 0x00BCC150>

class BaseWith__str__(object):
    def __init__(self, value):
        print 'init'
        self.value = value
    def f1(self):
        print 'f1'
    def __str__(self, *args, **kwargs):
        return "the ret is:" + self.value

print BaseWith__str__("testValue") #the ret is:testValue

class BaseWith__unicode__(object):
    def __init__(self, value):
        print 'init'
        self.value = value
    def f1(self):
        print 'f1'
    def __unicode__(self, *args, **kwargs):
        return "the ret is:" + self.value

print BaseWith__unicode__("testValue") #the ret is:testValue