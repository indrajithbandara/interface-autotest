import os
import sys

from string import Template


def produceModel(parameters):
    modelClass(parameters)
    defModelHBM(parameters)


def produceService(parameters):
    serviceInter(parameters)
    serviceImpl(parameters)


def produceDao(parameters):
    daoInter(parameters)
    daoImpl(parameters)


def modelClass(parameters):
    code = Template('''''package\n
public class ${className} {\n
${attribute}
${methods}
}
''')
    name = parameters[0]  # class name
    argv2 = parameters[1]
    attribute = ""
    methods = ""
    properties = argv2.split(",")
    for x in range(len(properties)):
        prop = properties[x].split(":")
        propType = prop[1]
        propName = prop[0]
        attribute += "\tprivate " + propType + " " + propName + ";\n"
        methods += "\tpublic " + propType + " set" + propName.capitalize() + "(" + propType + " " + propName + ") {\n\t\tthis." + propName + " = " + propName + ";\n\t}\n"
        methods += "\tpublic void get" + propName.capitalize() + "() {\n\t\treturn " + propName + ";\n\t}\n"

    fileStr = code.substitute(className=name, attribute=attribute, methods=methods)
    saveFile(fileStr, name + ".java")


def defModelHBM(parameters):
    code = Template('''''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-mapping PUBLIC
    "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
    "http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd">

<hibernate-mapping>
    <class name="${name}" table="${name}">
${property}
    </class>
</hibernate-mapping>
''')
    name = parameters[0]  # class name
    argv2 = parameters[1]
    property = ""
    properties = argv2.split(",")
    for x in range(len(properties)):
        prop = properties[x].split(":")
        property += "\t\t<property name=\"" + prop[0] + "\" />\n"

    fileStr = code.substitute(name=name, property=property)
    saveFile(fileStr, name + ".hbm.xml")


def serviceInter(parameters):
    code = Template('''''package\n
public interface ${name}Service extends GenericManager<${name}, Integer> {

}
''')
    name = parameters[0]
    fileStr = code.substitute(name=name)
    saveFile(fileStr, name + "Service.java")


def serviceImpl(parameters):
    code = Template('''''package\n
public class ${name}ServiceImpl extends GenericManagerImpl<${name}, Integer>
        implements ${name}Service{

    private ${name}Dao ${namelow}Dao;

    public ${name}ServiceImpl(${name}Dao ${namelow}Dao){
        super(${namelow}Dao);
        this.${namelow}Dao = ${namelow}Dao;
    }
}
''')
    name = parameters[0]
    namelow = name.lower()
    fileStr = code.substitute(name=name, namelow=namelow)
    saveFile(fileStr, name + "ServiceImpl.java")


def daoInter(parameters):
    code = Template('''''package\n
public interface ${name}Dao extends GenericDao<${name}, Integer> {

}
''')
    name = parameters[0]
    fileStr = code.substitute(name=name)
    saveFile(fileStr, name + "Dao.java")


def daoImpl(parameters):
    code = Template('''''package\n
public class ${name}ServiceImpl extends GenericManagerImpl<${name}, Integer>
        implements ${name}Service{

    private ${name}Dao ${namelow}Dao;

    public ${name}ServiceImpl(${name}Dao ${namelow}Dao){
        super(${namelow}Dao);
        this.${namelow}Dao = ${namelow}Dao;
    }
}
''')
    name = parameters[0]
    namelow = name.lower()
    fileStr = code.substitute(name=name, namelow=namelow)
    saveFile(fileStr, name + "DaoImpl.java")

def httpGetImplement(parameters,assertobj):
    code = Template('''''
# -*- coding: utf-8 -*-
# encoding:utf-8
import httplib
import unittest


class testcase_api_httpget(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    # change user interface for bazaar_utils & access story
    def test_${name}(self):
        try:

            self.httpClient.request('GET', '/client/v1/get_order?user_id=11452&order_id=12173793044055')
            # response object
            response = self.httpClient.getresponse()
            print response.status
            statucode = response.status
            print response.read()
            if statucode == '200' or statucode == '201':
                print "The get_order_list status is 200 or 201"
                ${assertobj}
            else:
                raise "The get_order_list has exception"
                print response.reason
                print response.read()
                # self.assertEqual(statucode, 200,'incorrect default size')
        except Exception, e:
            print e
        finally:
            if self.httpClient:
                self.httpClient.close()
''')
    name = parameters[0]
    namelow = name.lower()
    fileStr = code.substitute(name=name, namelow=namelow,assertobj=assertobj)
    saveFile(fileStr, name + "HttpGetImpl.py")




def saveFile(code, path):
    print path
    f = open(path, 'w')
    f.write(code)
    f.close()


# param1 ModelName
# param2 Properties
def main():
    parameters = sys.argv[1:]
    number = len(parameters)
    if (number < 2):
        print "Error parameters"
    else:
        produceModel(parameters);
        produceService(parameters);
        produceDao(parameters);
        httpGetImplement(parameters,"assertdemo");


if __name__ == "__main__":
    main()