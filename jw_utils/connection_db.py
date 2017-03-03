# -*- encoding: utf8 -*-

'''
Copyright 2016 JointWisdom Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import MySQLdb

import ConfigParser
import psycopg2
config=ConfigParser.ConfigParser()
# with open('./test-config/testcfg.cfg','r') as cfgfile:
#    config.readfp(cfgfile)
#    name=config.get('info','nam')
#    age=config.get('info','age')
#    print name
#    print age
with open('../test-config/systemcfg.properties', 'r') as cfg:
       config.readfp(cfg)
       # print config.get('config', 'username')
       print config.get('config', 'jw-host')
       print config.get('config', 'jw-port')
       print config.get('config', 'jw-user')
       print config.get('config', 'jw-passwd')
       print config.get('config', 'jw-db')

       jwhost=config.get('config', 'jw-host')
       jwport=config.get('config', 'jw-port')
       jwuser= config.get('config', 'jw-user')
       jwpasswd= config.get('config', 'jw-passwd')
       jwdb= config.get('config', 'jw-db')
   # config.set('info','gender','male')
# config.set('info','age','21')
# age=config.get('info,'age')
# print name
# print age


db = {
    'host': jwhost,
    'port': jwport,
    'user': jwuser,
    'passwd': jwpasswd,
    'db': jwdb,
    #'charset': 'utf8',
}

conn = psycopg2.connect(database="jw_platform", user="platform", password="123456", host="192.168.18.206", port="5432")
cur = conn.cursor()

# conn = MySQLdb.connect(**db)
# cur = conn.cursor()


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
    select_sql = "select * from BS_SYS_DAY"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result

def select1():
    """
       查询记录
    """
    select_sql = "select * from BS_SYS_USER"
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

#testcase
def selectIFD_EXPINPUT():
    """
       查询记录
    """
    select_sql = "select * from IFD_EXPINPUT"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result

def selectIFD_EXPOUTPUT():
    """
       查询记录
    """
    select_sql = "select * from IFD_EXPOUTPUT"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result

def selectIFD_EXPASSERT():
    """
       查询记录
    """
    select_sql = "select * from IFD_EXPASSERT"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result

#interface
def selectIFD_INTERFACEDEF():
    """
       查询记录
    """
    select_sql = "select * from IFD_INTERFACEDEF"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result

def selectIFD_INFPARAM():
    """
       查询记录
    """
    select_sql = "select * from IFD_INFPARAM"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result

def selectIFD_EXAMPLEDEF():
    """
       查询记录
    """
    select_sql = "select * from IFD_EXAMPLEDEF"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result

#DTO table
def selectIFD_DTODEF():
    """
       查询记录
    """
    select_sql = "select * from IFD_DTODEF"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result
def selectIND_DTOFIELD():
    """
       查询记录
    """
    select_sql = "select * from IND_DTOFIELD"
    cur.execute(select_sql)
    result = cur.fetchall()

    print result


#interface
def selectIFD_INTERFACEDEFOneRecord():
    """
       查询记录
    """
    select_sql = "select * from IFD_INTERFACEDEF"
    cur.execute(select_sql)
    result = cur.fetchall()
    # print result
    # for row in result:
    #     fname = row[0]
    #     lname = row[5]
    #     print row[0]
    #     print lname
        # # 打印结果
        # print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
        #      (fname, lname, age, sex, income )
    return result
#interface
def selectIFD_EXPASSERTOneRecord():
    """
       查询记录
    """
    select_sql = "select * from IFD_EXPASSERT"
    cur.execute(select_sql)
    result = cur.fetchall()

    return result

def selectIFD_EXPASSERTOneonly(id):
    """
       query record from one table
    """
    select_sql = "select * from IFD_EXPASSERT where id=%s"
    print "the sql statement is ->",select_sql
    cur.execute(select_sql,[id])
    result = cur.fetchone()
    if result == None: return "None"
    return result


#==================================================================================
def getIFD_INTERFACEDEF_All():
    """
       query record---> query all record from IFD_INTERFACEDEF table
    """
    select_sql = "select * from IFD_INTERFACEDEF"
    print "the getIFD_INTERFACEDEF_All sql statement is ->",select_sql
    cur.execute(select_sql)
    result = cur.fetchall()
    if result == None: return "N"
    return result

def getIFD_EXAMPLEDEF_From_IFD_INTERFACEDEF(INTER_NAME):
    """
       query record from one table
    """
    print " the pars INTER_NAME is ===========>",INTER_NAME
    select_sql = "SELECT * FROM jw_platform.IFD_EXAMPLEDEF where INFNM=%s"
    print "the getIFD_EXAMPLEDEF_From_IFD_INTERFACEDEF sql statement is ->",select_sql
    cur.execute(select_sql,[INTER_NAME])
    result = cur.fetchone()
    if result == None: return "N"
    return result

def getIFD_EXPINPUT_From_EXAMPLEDEF_ID(EXAMPLEDEF_ID):
    """
       query record from one table
    """
    print " the pars EXAMPLEDEF_ID is ===========>",EXAMPLEDEF_ID
    select_sql = "SELECT * FROM jw_platform.IFD_EXPINPUT where EXAMPLEDEF_ID=%s"
    print "the getIFD_EXPINPUT_From_EXAMPLEDEF_ID sql statement is ->",select_sql
    cur.execute(select_sql,str(EXAMPLEDEF_ID))
    result = cur.fetchone()
    print " the none result ",result
    if result == None: return "N"
    return result

def getIFD_EXPOUTPUT_From_EXAMPLEDEF_ID(EXAMPLEDEF_ID):
    """
       query record from one table
    """
    print " the pars EXAMPLEDEF_ID is ===========>",EXAMPLEDEF_ID
    select_sql = "SELECT * FROM jw_platform.IFD_EXPOUTPUT where EXAMPLEDEF_ID=%s"
    print "the getIFD_EXPOUTPUT_From_EXAMPLEDEF_ID sql statement is ->",select_sql
    cur.execute(select_sql,[EXAMPLEDEF_ID])
    result = cur.fetchone()
    if result == None: return "N"
    return result

def getIFD_EXPASSERT_From_EXAMPLEDEF_ID(EXAMPLEDEF_ID):
    """
       query record from one table
    """
    print " the pars EXAMPLEDEF_ID is ===========>",EXAMPLEDEF_ID
    select_sql = "SELECT * FROM jw_platform.IFD_EXPASSERT where EXAMPLEDEF_ID=%s"
    print "the getIFD_EXPASSERT_From_EXAMPLEDEF_ID sql statement is ->",select_sql
    cur.execute(select_sql,EXAMPLEDEF_ID)
    result = cur.fetchone()
    if result == None: return "N"
    return result


def main():

     # getIFD_INTERFACEDEF_All()
     result=getIFD_INTERFACEDEF_All()
     for inter_row in result:
        print "===========inter_row row[3]->",inter_row[3]
        result_case=getIFD_EXAMPLEDEF_From_IFD_INTERFACEDEF("testcase1")
        print "===testcase ID ###################===",result_case[0]
        result_input=getIFD_EXPINPUT_From_EXAMPLEDEF_ID(result_case[0])
        result_output=getIFD_EXPOUTPUT_From_EXAMPLEDEF_ID(result_case[0])
        result_assert=getIFD_EXPASSERT_From_EXAMPLEDEF_ID(result_case[0])
        print " the result_input is ===>",result_input[3]
        print " the result_output is ===>",result_output[2]
        print " the result_assert is ===>",result_assert[3]
        #resultoneb = case_row[3].split(";")
    # insert()
    # select()
    # select1()
    # update()
    # delete()
    # selectIFD_EXPINPUT()
    # selectIFD_EXPOUTPUT()
    # selectIFD_EXPASSERT()


    # selectIFD_INTERFACEDEF()
    # result=selectIFD_INTERFACEDEFOneRecord()
    # for row in result:
    #     fname = row[0]
    #     lname = row[5]
    #     print "===========row[3]->",row[3]
    #     print lname
    #     resultone=selectIFD_EXPASSERTOneonly(row[3])
    #     print "===only you========",resultone[3]
    #     resultoneb = resultone[3].split(";")
    #     print "======++++++resultoneb",resultoneb
    #     for each_list in resultoneb:
    #         print (each_list);
    # print "===========",resultone

    # resultassert=selectIFD_EXPASSERTOneRecord()
    # for row in resultassert:
    #     print row[3]
    # resultone=selectIFD_EXPASSERTOneonly(1)
    # print resultone
    # selectIFD_EXAMPLEDEF()
    # selectIFD_INFPARAM()
    #
    # selectIFD_DTODEF()
    # selectIND_DTOFIELD()



if __name__ == "__main__":
    main()
