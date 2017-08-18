#coding:utf-8
a,b,c = 1,2,3
d,e,f = None,None,None
'''
统计某个attribute在列表中出现的次数
'''
if [a,b,c,d,e,f].count(None) == 3:
    print 'yes.'

print [a,b,c,d,e,f].count(1)  #1

if [a,b,c,d,e,f].count(None) > 0:
    print 'None exist.'