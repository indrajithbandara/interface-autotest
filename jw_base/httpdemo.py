#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py

import urllib
import urllib2
import unittest
import json
import httplib


class testcase_api_http(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    def test_testcaseGet(self):
        try:
            self.httpClient.request('GET', '/client/v1/get_order?user_id=11452&order_id=12173793044055')
            # response object
            print "------------------>/client/v1/get_order?user_id=11452&order_id=12173793044055"
            response = self.httpClient.getresponse()
            print response.status
            statucode = response.status
            print response.read()
            if statucode == '200' or statucode == '201':
                print "The get_order_list status is 200 or 201"
                #assertpostdemo();
            else:
                raise "The get_order_list has exception"
                print response.reason
                print response.read()
                # self.assertEqual(statucode, 200,'incorrect default size')
        except Exception, e:
            print e

    # change user interface for bazaar_utils & access story
    def test_testcasePost(self):
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





