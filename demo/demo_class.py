class Base(object):
    pass
print(type(Base)) #<type 'type'>
print(type(Base())) #<class '__main__.Base'>
##
me = "ansible-playbook -i ivn /export/Shell/testPlaybook.yaml" 
target = me.split('-')
print target
print target[10]