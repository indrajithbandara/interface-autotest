#!/usr/bin/env python
#coding=utf8
#!/usr/bin/env python
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')

r.get('foo')
print r.get('foo')
'bar'

import redis

def redis_node():
    node =redis.StrictRedis(host='localhost',port=6379)
    node.set("name_test","admin")
    print node.get("name_test")

redis_node()


# sed 匹配100_1000或bigger_1000
# sed -n '/100_1000\|bigger_1000/p' 20160220
# sed -n '/1001000∥bigger1000/p' 20160220
#
# awk匹配100_1000或bigger_1000
# 默认是$0匹配，所以写不写均可
# awk '/100_1000/||/bigger_1000/{print $0}' 20160220 | head
# awk '$0~/100_1000/||/bigger_1000/{print $0}' 20160220 | head
#
# grep匹配100_1000或bigger_1000 -E选项表示扩展的正则表达式
# grep -E '(100_1000|bigger_1000)' 20160220 | head
#
# 二、匹配与
#
# sed匹配与
# sed -n '/19000/{/100_1000/p}' 20160220 | head
#
# awk匹配与
# awk '/19000/&&/100_1000/{print $0}' 20160220 | head
# awk '$0~/19000/&&/100_1000/{print $0}' 20160220 | head
#
# grep匹配与
# grep -E '(19000.*100_1000|100_1000.*19000)' 20160220 | head

fs = [ lambda n: i+n for i in range(5) ]

for k in range(5):
    print "fs[%d]: " %k,fs[k](4)