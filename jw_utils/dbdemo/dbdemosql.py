# -*- coding:utf-8 -*-  
import MySQLdb

#库名：python;表名：students

conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='python',charset='utf8')
cursor = conn.cursor()
count = cursor.execute('select mail from students')

mail_list=[]
#获取所有结果
results = cursor.fetchall()
result=list(results)
for r in result:
    #print 'mail:%s ' % r
    mail_list.append(('<span style="color:#ff0000;">%s' % r</span>))
print mail_list

#游标归零，默认mode='relative'
cursor.scroll(0,mode='absolute')
count = cursor.execute('select name from students')

name_list=[]
results=cursor.fetchall()
result=list(results)
for r in result:
    #print '%s' % r
    #print type('%s' % r)
    name_list.append(('%s' % r))
#for i in range(6):
#    print name_list[i]

conn.close()
