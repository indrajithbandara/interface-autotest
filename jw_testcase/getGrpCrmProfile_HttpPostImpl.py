
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
import loginSessionKey
reload(sys)
sys.setdefaultencoding('utf8')

#Post http interface testing method
class testcase_getGrpCrmProfile_httppostImpl(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        #apihostpath="/3160001RA-1.0.0-SNAPSHOT"
        httpClient = None
        self.httpClient = httplib.HTTPConnection('192.168.18.217', 18080, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    def test_getGrpCrmProfile(self):
            print "The InterfaceApi POST Request staring............................"
            params ={"displayData":"","id":0,"logAbstractInfo":"","logDiffer":[],"logInfoDto":"","requestCommonDto":{"sessionKey":"","sysTypeName":"","token":"","tokenStatus":"","tracerId":"","unitUid":"","validReqDtoStatus":""}}
            jsondump_params=json.dumps(params)
            print " @@@@@@@@@@@@@@@@@the requestjson >>>>>>>>>>>>>> ",jsondump_params
            sessionKeyStr=loginSessionKey.getLoginSessionKey()
            print " @@@@@@@@@@@@@@@@@the sessionkey >>>>>>>>>>>>>>",sessionKeyStr
            tokenStr=loginSessionKey.getTokenKey(sessionKeyStr)
            print " @@@@@@@@@@@@@@@@@the tokenStr >>>>>>>>>>>>>>",tokenStr
            headers = {"Content-type": "application/json; charset=UTF-8" , "Accept": "*/*", "jw_data": sessionKeyStr, "jw_token": tokenStr}
            self.httpClient.request("POST", "/3160001RA-1.0.0-SNAPSHOT/bs/3510010/GrpCrmProfile/getData",jsondump_params, headers)

            #response is HTTPResponse Object
            response = self.httpClient.getresponse()
            print response.reason
            reponstr = response.read()
            responsejsonStr={"responseCommonDto":{"errorLevel":"","lans":"","message":"","resultCode":"","sessionKey":"","token":"","tracerId":""},"resultData":{"crmprofile":{"altNm":"","birthday":"","birthdayLunard":0,"birthdayLunarm":0,"birthdayLunary":0,"chainUid":"","cityId":0,"countryId":0,"createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","educationId":0,"firstNm":"","gender":"","id":0,"indexNm":"","languageId":0,"lastNm":"","memo":"","middleNm":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","nationId":0,"occupationId":0,"parentEntityLock":"","profileNo":"","profileTyp":"","provinceId":0,"rcityId":0,"rcountryId":0,"rprovinceId":0,"secretFlg":"","sleepFlg":"","statusFlg":"","titleId":0,"version":0},"crmprofileaddress":{"address1":"","address2":"","address3":"","addressFlg":"","chainUid":"","cityId":0,"commonFlg":"","countryId":0,"createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","defaultFlg":"","id":0,"modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","parentEntityLock":"","postNo":"","profileNo":"","provinceId":0,"statusFlg":"","version":0,"zoneNo":""},"crmprofileblacklist":{"blklstcxlrsnId":0,"blklsttypId":0,"chainUid":"","createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","id":0,"modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","note":"","parentEntityLock":"","profileNo":"","statusFlg":"","version":0},"crmprofilecertificate":{"certificate_idcd":"","certificatetypId":0,"chainUid":"","countryId":0,"createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","defaultFlg":"","expiryDt":"","id":0,"issueDt":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","parentEntityLock":"","profileNo":"","statusFlg":"","version":0},"crmprofileclass":{"chainUid":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","id":0,"modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","note":"","parentEntityLock":"","prfclsId":0,"prfsubclsId":0,"profileNo":"","statusFlg":"","unitUid":"","version":0,"vipId":0},"crmprofilecompany":{"chainUid":"","contractComp":"","createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","defaultFlg":"","department":"","id":0,"modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","parentEntityLock":"","positionId":0,"profileNo":"","statusFlg":"","version":0,"workComp":"","worktitleId":0},"crmprofilecontactway":{"":{"chainUid":"","contactFlg":"","contact_ctno":"","contacttypId":0,"countryId":0,"createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","defaultFlg":"","id":0,"modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","note":"","parentEntityLock":"","profileNo":"","receiptFlg":"","statusFlg":"","version":0,"zoneNo":""}},"crmprofilenotice":{"chainUid":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","defaultFlg":"","id":0,"memo":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","noticeFlg":"","noticeTitle":"","parentEntityLock":"","postypId":0,"profileNo":"","statusFlg":"","subDto":{"itemIds":[]},"unitUid":"","version":0}}}
            print "@@@@@@@@@@@responsejsonStr@@@@@@@@@@@@",responsejsonStr
            statucode=response.status
            print "the response.status is --->",statucode
            self.assertEqual(statucode, 200);self.assertNotEqual(statucode, 201)
            if statucode==200 or statucode==201:
                print "The get_order_list status is 200 or 201"
                print " the repoStr >>>>>>>>>>>>>",response.read()
                dictstr=json.dumps(response.read())
                #print "##########dict######################",dictstr
                print "##########dict######################",reponstr
                dictstr=json.loads(reponstr)
                for i in dictstr:
                    print "#@@@@@@@@@@@@@dictstr[%s]=" % i,dictstr[i]
                    if str(responsejsonStr).find(i) == -1:
                         print "No 'filed in reponse str' here!"
                    else:
                         print "Found ' field str inclued ' in the string."

