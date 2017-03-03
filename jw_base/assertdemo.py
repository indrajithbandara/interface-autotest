#  -*- coding:utf-8 -*-
import json
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2,sort_keys=True)
print d1
print d2
print d3
print d1==d2
print d1==d3

import json
obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
encodedjson = json.dumps(obj)
print repr(obj)
print encodedjson
s='com.jw.platform'
print " reverease str is ->",s[::-1]
s.index('platform')
print "=========s.index('.')>",s.rindex('.')
#print str[-3:-1]

#s[s.find(".") + 1:]
print " reverease str ....is ->",s[::-1][0:s[::-1].find(".")]
strdemo=s[::-1][0:s[::-1].find(".")]
print strdemo[::-1]
info = 'abca'
print info.find('a')

"""
assertEqual(a, b)     a == b
assertNotEqual(a, b)     a != b
assertTrue(x)     bool(x) is True
assertFalse(x)     bool(x) is False
assertIs(a, b)     a is b     2.7
assertIsNot(a, b)     a is not b     2.7
assertIsNone(x)     x is None     2.7
assertIsNotNone(x)     x is not None     2.7
assertIn(a, b)     a in b     2.7
assertNotIn(a, b)     a not in b     2.7
assertIsInstance(a, b)     isinstance(a, b)     2.7
assertNotIsInstance(a, b)     not isinstance(a, b)     2.7
"""

#!/usr/bin/python
dict={"a":"apple","b":"banana","o":"orange"}

print "##########dict######################"
for i in dict:
    print "dict[%s]=" % i,dict[i]

print "###########items#####################"
for (k,v) in  dict.items():
    print "dict[%s]=" % k,v

print "###########iteritems#################"
for k,v in dict.iteritems():
    print "dict[%s]=" % k,v

print "###########iterkeys,itervalues#######"
for k,v in zip(dict.iterkeys(),dict.itervalues()):
    print "dict[%s]=" % k,v

# l = [(x,x) for x in xrange(10000)]
# d = dict(l)
#
# from time import clock
#
# t0=clock()
# for i in d:
#     t = i + d[i]
# t1=clock()
#
# for k,v in d.items():
#     t = k + v
# t2=clock()
#
# for k,v in d.iteritems():
#     t = k + v
# t3=clock()
#
# for k,v in zip(d.iterkeys(),d.itervalues()):
#     t = k + v
# t4=clock()
#
# print t1-t0, t2-t1, t3-t2, t4-t3

aDict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print '-----------dict-------------'
for d in aDict:
    print "%s:%s" %(d, aDict[d])

print '-----------item-------------'
for (k,v) in aDict.items():
    print '%s:%s' %(k, v)
#效率最高
print '------------iteritems---------'
for k,v in aDict.iteritems():
    print '%s:%s' % (k, v)
#最笨的方法
print '---------iterkeys---------------'
for k in aDict.iterkeys():
    print '%s:%s' % (k, aDict[k])

print '------------iterkeys, itervalues----------'
for k,v in zip(aDict.iterkeys(), aDict.itervalues()):
    print '%s:%s' % (k, v)

#-*- coding:utf8 -*-
from timeit import timeit
from dis import dis

#用type和isinstance分别判断{'s'}是否属于set类型
def a():return type({'s'})is set
def b():return isinstance({'s'},set)
def c():return type({'s'})==set

time = [timeit(a),timeit(b),timeit(c)]

#打印结果
print 'result:\n%s %s %s\n'%(a(),b(),c())

#打印时间
print 'time:\n%s\n'%( ''.join([str(_)+'\n' for _ in time]) )

#打印指令
print 'orders:\n'
dis(a)
print '\n'
dis(b)
print '\n'
dis(c)

import sys
from dis import dis


def func():
    f = sys._getframe(0)
    print f.f_lasti
    print f.f_back
    yield 1

    print f.f_lasti
    print f.f_back
    yield 2


a = func()
dis(func)
a.next()
a.next()


import json

dict_ = {1:2, 3:4, "55":"66"}

# test json.dumps

print type(dict_), dict_
json_str = json.dumps(dict_)
print "json.dumps(dict) return:"
print type(json_str), json_str

# test json.loads
print "\njson.loads(str) return"
dict_2 = json.loads(json_str)
print type(dict_2), dict_2