# -*- encoding: utf8 -*-
'''
Created on 2016-11-11
updated on 2016-3-16
@author: cuijun
Description:数据库操作demo
'''
import psycopg2
import ConfigParser

config=ConfigParser.ConfigParser()
with open('../test-config/systemcfg.properties', 'r') as cfg:
    config.readfp(cfg)
    # print config.get('config', 'username')
    print config.get('pgconfig', 'jw-host')
    print config.get('pgconfig', 'jw-port')
    print config.get('pgconfig', 'jw-user')
    print config.get('pgconfig', 'jw-passwd')
    print config.get('pgconfig', 'jw-db')

    jwhost=config.get('pgconfig', 'jw-host')
    jwport=config.get('pgconfig', 'jw-port')
    jwuser= config.get('pgconfig', 'jw-user')
    jwpasswd= config.get('pgconfig', 'jw-passwd')
    jwdb= config.get('pgconfig', 'jw-db')

conn = psycopg2.connect(database="postgres", user="pgadmin", password="klip2[gE%dad5", host="192.168.18.206", port="5432")
cur = conn.cursor()
# cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
# cur.execute("SELECT * FROM product_category;")
cur.execute("SELECT * FROM pg_am;")
rows = cur.fetchall()        # all rows in table
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()