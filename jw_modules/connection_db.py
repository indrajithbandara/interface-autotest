# -*- encoding: utf8 -*-
'''
Created on 2016-1-26
updated on 2016-3-16
@author: xuhao
Description:数据库操作demo
'''
import MySQLdb

db = {
    'host': '10.6.5.234',
    'port': 3306,
    'user': 'root',
    'passwd': 'uvhxqaMjMPjhJZw3',
    'db': 'test',
    'charset': 'utf8',
}
conn = MySQLdb.connect(**db)
cur = conn.cursor()


def insert():
    """
       插入2条记录
    """
    insert_sql = "insert into hao (name) VALUES ( %s)"
    name_list = ["小明", "小张"]
    for item in name_list:
        cur.execute(insert_sql, (item, ))
    conn.commit()

def select():
    """
       查询记录
    """
    select_sql = "select * from hao"
    cur.execute(select_sql)
    result = cur.fetchall()
    print result

def delete():
    """
       删除name是小明的记录
    """
    delete_sql = "delete from hao WHERE name=%s"
    cur.execute(delete_sql, ("小明",))
    conn.commit()


def update():
    """
       把小张更新成小张张
    """
    update_sql = "update hao set name = %s where name = %s"
    cur.execute(update_sql, ("小张张", "小张"))
    conn.commit()

def main():
    insert()
    select()
    update()
    delete()

if __name__ == "__main__":
    main()
