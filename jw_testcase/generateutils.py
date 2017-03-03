# -*- coding: utf-8 -*-
# encoding:utf-8
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

import os
import sys
sys.path.append("../")
sys.path.append("../jw_utils")
sys.path.append("../jw_base")
from string import Template
from jw_utils import connection_db

def httpGetImplement(testcase,assertStr,testcaseURL,interIP):
    code = Template('''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
import time,os,sys,datetime,unittest
import os
sys.path.append("../")
sys.path.append("../jw_modules")
import httplib
import unittest
from jw_utils.logUtils import *



class testcase_api_httpget_${testcase}(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('${interIP}', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    # change user interface for bazaar_utils & access story
    def test_${testcase}(self):
            self.httpClient.request('GET', '${testcaseURL}')
            # response object
            response = self.httpClient.getresponse()
            #print response.status
            statucode = response.status
            #print response.read()
            print "the response.status is --->",response.status,response.read()
            self.assertEqual(statucode, 200);self.assertNotEqual(statucode, 201)
            if statucode == 200 or statucode == 201:
                print "The get_order_list status is 200 or 201"
                #${assertStr}();
                print " the ${assertStr} ===========>", ${assertStr}
                ${assertStr}
                # for each_list in ${assertStr}:
                #     print (each_list);
            else:
                raise "The get_order_list has exception"
                print response.reason
                print response.read()
                # self.assertEqual(statucode, 200,'incorrect default size')

''')
    print "##############testcase ##########",testcase,assertStr
    # name = testcase
    # namelow =name.lower()
    # name = "abc"
    # namelow =name.lower()
    fileStr = code.substitute(testcase=testcase,assertStr=assertStr,testcaseURL=testcaseURL,interIP=interIP)
    saveFile(fileStr, testcase + "HttpGetImpl.py")


def httpPostImplement(assertobj,restURL):
    code = Template('''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
import time,os,sys,datetime,unittest
import os
sys.path.append("../")
sys.path.append("../jw_modules")
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
            self.httpClient.request('GET', '${restURL}')
            # response object
            print "------------------>${restURL}"
            response = self.httpClient.getresponse()
            print response.status
            statucode = response.status
            print response.read()
            if statucode == 200 or statucode == 201:
                print "The get_order_list status is 200 or 201"
                ${assertobj};
            else:
                raise "The get_order_list has exception"
                print response.reason
                print response.read()
                # self.assertEqual(statucode, 200,'incorrect default size')


''')
    # name = parameters[0]
    # namelow = name.lower()
    name = "testcasename001"
    namelow ="testcasename001"
    fileStr = code.substitute(name=name, namelow=namelow,assertobj=assertobj,restURL=restURL)
    saveFile(fileStr, name + "HttpPostImpl.py")

def httpPostSendImplement(parameters):
    code = Template('''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
import time,os,sys,datetime,unittest
import os
sys.path.append("../")
sys.path.append("../jw_modules")
import httplib
import unittest
import json
import urllib


class testcase_api_httpsendpost(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    def test_${name}(self):
            f=open("")
            strcreateoder=json.load(f)
            print strcreateoder
            params = urllib.urlencode(strcreateoder)
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            self.httpClient.request('POST', "", params, headers)
            #response是HTTPResponse对象
            response = self.httpClient.getresponse()
            print response.status
            statucode=response.status
            print response.read()
            if statucode==200 or statucode==201:
                print "The get_order_list status is 200 or 201"
            else:
                raise "The interface has exception"
                print response.reason
                print response.read()
                #self.assertEqual(statucode, 200,'incorrect default size')

''')
    # name = parameters[0]
    # namelow = name.lower()
    name = "testcasena03"
    namelow ="testcasena03"
    fileStr = code.substitute(name=name, namelow=namelow,assertobj=parameters)
    saveFile(fileStr, name + "PostImpl.py")



def httpPostMethod(testcase,assertStr,testcaseURL,interIP):
    code = Template('''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
import time,os,sys,datetime,unittest
import os
sys.path.append("../")
sys.path.append("../jw_modules")
import httplib
import unittest
import json
import urllib

#Post http interface testing method
class testcase_api_${testcase}(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('${interIP}', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    def test_${testcase}(self):
            f=open("jsondata.json")
            strcreateoder=json.load(f)
            print strcreateoder
            params = urllib.urlencode(strcreateoder)
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            self.httpClient.request('POST', "${testcaseURL}", params, headers)
            #response is HTTPResponse Object
            response = self.httpClient.getresponse()
            #print response.status
            statucode=response.status
            print "the response.status is --->",response.status,response.read()
            self.assertEqual(statucode, 200);self.assertNotEqual(statucode, 201)
            if statucode==200 or statucode==201:
                print "The get_order_list status is 200 or 201"
                ${assertStr}
            else:
                raise "The interface has exception"
                print response.reason
                print response.read()
                #self.assertEqual(statucode, 200,'incorrect default size')

''')
    # name = parameters[0]
    # namelow = name.lower()
    # name = "testcasename003"
    # namelow ="testcasename003"
    fileStr = code.substitute(testcase=testcase,assertStr=assertStr,testcaseURL=testcaseURL,interIP=interIP)
    saveFile(fileStr, testcase + "PostImpl.py")



def saveFile(code, path):
    print path
    f = open(path, 'w')
    f.write(code)
    f.close()


# param1 ModelName
# param2 Properties
def main():
    # parameters = sys.argv[1:]
    # number = len(parameters)
    # if (number < 2):
    #     print "Error parameters"
    # else:
    #     httpGetImplement("assertgetdemo");
    #     httpPostImplement("assertpostdemo","/client/v1/get_order?user_id=11452&order_id=12173793044055");
    s = Template('There  ${moneyType} is  ${money}')
    print s.substitute(moneyType = 'Dollar',money=12)
    result=connection_db.selectIFD_INTERFACEDEFOneRecord();
    for row in result:
        # fname = row[0]
        # lname = row[5]
        strtestname=''.join(row[2])
        print " the row[2] is############ ->",strtestname
        resultone=connection_db.selectIFD_EXPASSERTOneonly(row[3])
        # strassertname=''.join(resultone[3])
        strassertname=resultone[3]
        strtesttype=row[7]
        restfulName=row[5]
        print " the resultone[3] is############ ->",strassertname,strtesttype

        if "get" in strtesttype:
                if strassertname != "e":
                    httpGetImplement(strtestname,strassertname,restfulName,"open09.edaixi.cn1111111");
                else:
                    print "the aassert is none value..."
        else:
                if strassertname != "e":
                     # httpPostImplement("testpost","/client/v1/get_order?user_id=11452&order_id=12173793044055");
                     httpPostMethod(strtestname,strassertname,restfulName,"open09.edaixi.cn1111111");
                else:
                    print "the aassert is none value..."

            # print " the resultone is ==============->",resultone[3]
        # if "e" in resultone[3]:
        #     print "this is nose value for db"
        # else:
        #     print "this ==###########>", httpGetImplement(row[2],resultone[3]);



if __name__ == "__main__":
    main()
