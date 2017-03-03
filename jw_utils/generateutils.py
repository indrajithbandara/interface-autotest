# -*- coding: utf-8 -*-
# encoding:utf-8
import os
import sys

from string import Template


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
    name = "testcasename002"
    namelow ="testcasename002"
    fileStr = code.substitute(name=name, namelow=namelow,assertobj=assertobj)
    saveFile(fileStr, name + "HttpGetImpl.py")


def httpPostImplement(parameters,assertobj):
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
    # name = parameters[0]
    # namelow = name.lower()
    name = "testcasename001"
    namelow ="testcasename001"
    fileStr = code.substitute(name=name, namelow=namelow,assertobj=assertobj)
    saveFile(fileStr, name + "HttpPostImpl.py")


def httpPostSendImplement(parameters,assertobj):
    code = Template('''''
# -*- coding: utf-8 -*-
# encoding:utf-8
import httplib
import unittest

try:

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
    if statucode=='200' or statucode=='201':
         print "The get_order_list status is 200 or 201"
    else:
         raise "The interface has exception"
         print response.reason
         print response.read()
         #self.assertEqual(statucode, 200,'incorrect default size')
    except Exception, e:
         print e
''')
    # name = parameters[0]
    # namelow = name.lower()
    name = "testcasename003"
    namelow ="testcasename003"
    fileStr = code.substitute(name=name, namelow=namelow,assertobj=assertobj)
    saveFile(fileStr, name + "HttpPostImpl.py")


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
        httpGetImplement(parameters,"assertdemo");


if __name__ == "__main__":
    main()
