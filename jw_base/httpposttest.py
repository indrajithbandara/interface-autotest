#!/usr/bin/env python
#coding=utf8
import httplib, urllib,json

httpClient = None
try:
    # jsonstr='{"orderColumn":"id","dir":"asc","languages":"\'1\',\'0\'","pageStart":"0","pageLength":"20"}'
    # object = json.load(jsonstr)
    fjson=open("jsondata.json")
    jsonstr=json.load(fjson)
    jsondump=json.dumps(jsonstr)
    print "the jsondump is --->",jsondump
    #params = urllib.urlencode(jsondump)
    headers = {"Content-type": "application/json; charset=UTF-8" , "Accept": "*/*", "jw_data": "9339f5d8-ce13-410a-8bf4-f5e00b654177"}

    httpClient = httplib.HTTPConnection("192.168.18.33", 8080, timeout=20)
    httpClient.request("POST", "/wisdomBsWeb/bs/BsSysUser/userListGetData", jsondump, headers)

    response = httpClient.getresponse()
    print " the statuis is ->",response.status
    print response.reason
    print response.read()
    # print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
