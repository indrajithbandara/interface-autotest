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
    def test_testcasename002(self):
        try:
            print "this is my test unit for python "
                # self.assertEqual(statucode, 200,'incorrect default size')
        except Exception, e:
            print e
            #finally:
            #if self.httpClient:
            #self.httpClient.close()