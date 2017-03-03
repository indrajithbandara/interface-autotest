
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
class testcase_saveGrpCrmCorp_httppostImpl(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        #apihostpath="/3160001RA-1.0.0-SNAPSHOT"
        httpClient = None
        self.httpClient = httplib.HTTPConnection('192.168.18.217', 18080, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    def test_saveGrpCrmCorp(self):
            print "The InterfaceApi POST Request staring............................"
            params ={"displayData":"","logAbstractInfo":"","logInfoDto":"","originData":{"grpCrmCorp":{"address1":"","address2":"","address3":"","chainUid":"","childFlg":"","cityId":0,"contactNo":"","corpNm":"","corpNmEn":"","corpNmRef":"","corpNo":"","corptypId":0,"countryId":0,"createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","duns":"","id":0,"indexNm":"","industryId":0,"licenseNo":"","manageUnitUid":"","manageUserUid":"","memo":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","organizationCd":"","parentCorpNo":"","parentEntityLock":"","postNo":"","provinceId":0,"sleepFlg":"","statusFlg":"","taxNo":"","version":0,"zoneNo":""},"grpCrmCorpAddresss":[],"grpCrmCorpContacts":[],"grpCrmCorpContactways":[],"grpCrmCorpNotices":[]},"requestCommonDto":{"sessionKey":"","sysTypeName":"","token":"","tokenStatus":"","tracerId":"","unitUid":"","validReqDtoStatus":""},"submitData":{"grpCrmCorp":{"address1":"","address2":"","address3":"","chainUid":"","childFlg":"","cityId":0,"contactNo":"","corpNm":"","corpNmEn":"","corpNmRef":"","corpNo":"","corptypId":0,"countryId":0,"createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","duns":"","id":0,"indexNm":"","industryId":0,"licenseNo":"","manageUnitUid":"","manageUserUid":"","memo":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","organizationCd":"","parentCorpNo":"","parentEntityLock":"","postNo":"","provinceId":0,"sleepFlg":"","statusFlg":"","taxNo":"","version":0,"zoneNo":""},"grpCrmCorpAddresss":[],"grpCrmCorpContacts":[],"grpCrmCorpContactways":[],"grpCrmCorpNotices":[]}}
            jsondump_params=json.dumps(params)
            print " @@@@@@@@@@@@@@@@@the requestjson >>>>>>>>>>>>>> ",jsondump_params
            sessionKeyStr=loginSessionKey.getLoginSessionKey()
            print " @@@@@@@@@@@@@@@@@the sessionkey >>>>>>>>>>>>>>",sessionKeyStr
            tokenStr=loginSessionKey.getTokenKey(sessionKeyStr)
            print " @@@@@@@@@@@@@@@@@the tokenStr >>>>>>>>>>>>>>",tokenStr
            headers = {"Content-type": "application/json; charset=UTF-8" , "Accept": "*/*", "jw_data": sessionKeyStr, "jw_token": tokenStr}
            self.httpClient.request("POST", "/3160001RA-1.0.0-SNAPSHOT/bs/3520010/GrpCrmCorp/save",jsondump_params, headers)

            #response is HTTPResponse Object
            response = self.httpClient.getresponse()
            print response.reason
            reponstr = response.read()
            responsejsonStr={"responseCommonDto":{"errorLevel":"","lans":"","message":"","resultCode":"","sessionKey":"","token":"","tracerId":""},"resultData":{"grpCrmCorp":{"address1":"","address2":"","address3":"","chainUid":"","childFlg":"","cityId":0,"contactNo":"","corpNm":"","corpNmEn":"","corpNmRef":"","corpNo":"","corptypId":0,"countryId":0,"createTyp":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","duns":"","id":0,"indexNm":"","industryId":0,"licenseNo":"","manageUnitUid":"","manageUserUid":"","memo":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","organizationCd":"","parentCorpNo":"","parentEntityLock":"","postNo":"","provinceId":0,"sleepFlg":"","statusFlg":"","taxNo":"","version":0,"zoneNo":""},"grpCrmCorpAddresss":[],"grpCrmCorpContacts":[],"grpCrmCorpContactways":[],"grpCrmCorpNotices":[]}}
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

