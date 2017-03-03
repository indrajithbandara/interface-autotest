#!/usr/bin/env python
#coding=utf8

import httplib

httpClient = None

try:
    httpClient = httplib.HTTPConnection('localhost', 80, timeout=30)
    httpClient.request('GET', '/test.php')

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()