#!/usr/bin/env python
#coding=utf8
import httplib, urllib,json

# httpClient = None
# try:
#     # jsonstr='{"orderColumn":"id","dir":"asc","languages":"\'1\',\'0\'","pageStart":"0","pageLength":"20"}'
#     # object = json.load(jsonstr)
#     fjson=open("loginSessionKey.json")
#     jsonstr=json.load(fjson)
#     jsondump=json.dumps(jsonstr)
#     print "the jsondump is --->",jsondump
#     #params = urllib.urlencode(jsondump)
#     headers = {"Content-type": "application/json; charset=UTF-8" , "Accept": "*/*"}
#
#     httpClient = httplib.HTTPConnection("192.168.18.214", 18080, timeout=20)
#     httpClient.request("POST", "/3160001RA-1.0.0-SNAPSHOT/login", jsondump, headers)
#
#     response = httpClient.getresponse()
#     print " the statuis is ->",response.status,response.reason
#
#     repoStr=response.read()
#     print repoStr
#     #print "=========>",repoStr[repoStr.rfind("sessionKey")+13:repoStr.rfind("token")-3]
#     sessionKeyStr=repoStr[repoStr.rfind("sessionKey")+13:repoStr.rfind("token")-3]
#     #print response.read()
#     # print response.read()
#     print sessionKeyStr #get header information
# except Exception, e:
#     print e
# finally:
#     if httpClient:
#         httpClient.close()

global httpHostIP
global httpPort,timeOutDate

# import ConfigParser
# config=ConfigParser.ConfigParser()
# with open('../test-config/systemcfg.properties', 'r') as cfg:
#     config.readfp(cfg)
#     # print config.get('config', 'username')
#     httpHostIP=config.get('config', 'httpHostIP')
#     httpPort=config.get('config', 'httpPort')
#     timeOutDate=config.get('config', 'timeOutDate')
httpHostIP="192.168.18.214"
httpPort=18080
timeOutDate=20

def getLoginSessionKey():

    print "get LoginSession Key now........................."
    httpClient = None
    try:
       # jsonstr='{"orderColumn":"id","dir":"asc","languages":"\'1\',\'0\'","pageStart":"0","pageLength":"20"}'
       # object = json.load(jsonstr)
       fjson=open("loginSessionKey.json")
       jsonstr=json.load(fjson)
       jsondump=json.dumps(jsonstr)

       headers = {"Content-type": "application/json; charset=UTF-8" , "Accept": "*/*"}
       httpClient = httplib.HTTPConnection(httpHostIP, httpPort, timeout=timeOutDate)
       httpClient.request("POST", "/3160001RA-1.0.0-SNAPSHOT/login", jsondump, headers)

       response = httpClient.getresponse()
       print " the statuis is ->",response.status,response.reason

       repoStr=response.read()
       sessionKeyStr=repoStr[repoStr.rfind("sessionKey")+13:repoStr.rfind("token")-3]

       print " @@@@@@@@@@@@@@@@@@@@@@@@@the sessionKeyStr is :",sessionKeyStr
       return sessionKeyStr
    except  Exception, e:
       print e
    finally:
       if httpClient:
          httpClient.close()



def getTokenKey(sessionkeyStr):
    print "get token key now............................"
    httpClient = None
    try:
        # jsonstr='{"orderColumn":"id","dir":"asc","languages":"\'1\',\'0\'","pageStart":"0","pageLength":"20"}'
        # object = json.load(jsonstr)
        #print "the jsondump is --->",jsondump
        #params = urllib.urlencode(jsondump)
        payload = {}
        jsondump=json.dumps(payload)
        headers = {"Content-type": "application/json; charset=UTF-8" , "Accept": "*/*", "jw_data": sessionkeyStr}
        httpClient = httplib.HTTPConnection(httpHostIP, httpPort, timeout=timeOutDate)
        httpClient.request("POST", "/3160001RA-1.0.0-SNAPSHOT/bs/BsToken/getToken",jsondump, headers)

        response = httpClient.getresponse()
        print " the statuis is ->",response.status,response.reason
        repoStr=response.read()
        tokenKeyStr=repoStr[repoStr.rfind("token")+8:repoStr.rfind("tracerId")-3]
        #print repoStr
        #print "=========>",repoStr[repoStr.rfind("sessionKey")+13:repoStr.rfind("token")-3]
        #sessionKeyStr=repoStr[repoStr.rfind("sessionKey")+13:repoStr.rfind("token")-3]
        #print response.read()
        # print response.read()
        #print sessionKeyStr #get header information
        #print sessionKeyStr
        print " the tokenKeyStr is :",tokenKeyStr
        return tokenKeyStr
    except  Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == '__main__':
    #print getLoginSessionKey()
    sessionkey=getLoginSessionKey()
    print sessionkey
    print getTokenKey(sessionkey)


