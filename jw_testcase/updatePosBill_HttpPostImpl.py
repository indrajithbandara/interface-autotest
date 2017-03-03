
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
class testcase_updatePosBill_httppostImpl(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        #apihostpath="/3160001RA-1.0.0-SNAPSHOT"
        httpClient = None
        self.httpClient = httplib.HTTPConnection('192.168.18.217', 18080, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    def test_updatePosBill(self):
            print "The InterfaceApi POST Request staring............................"
            params ={"displayData":"","logAbstractInfo":"","logInfoDto":"","originData":{"acctId":0,"acctNo":"","afterPrintPage":0,"billAmount":0,"billId":0,"billNo":"","billOrigin":"","billOriginNo":"","billStus":"","billTranNo":"","billTyp":0,"blockNum":0,"chainUid":"","closeBy":"","closeByCd":"","closeByUid":"","closeDate":"","closePeriod":"","closeWsCd":"","closeWsId":0,"contacterNm":"","contacterTlno":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","createdWsCd":"","createdWsId":0,"discountAmount":0,"discountFlg":"","discountRate":0,"id":0,"insideBy":"","insideByCd":"","insideByUid":"","insideCd":"","insideDate":"","insideDept":"","insideDeptCd":"","insideDeptUid":0,"insideFlg":"","insideMemo":"","insideUid":0,"insideUnitCd":"","insideUnitUid":0,"makeAmount":0,"makeupFlg":"","marketTyp":0,"memo":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","modifiedWsCd":"","modifiedWsId":0,"openBy":"","openByCd":"","openByUid":"","openDate":"","openFlg":"","openPeriod":"","orgTyp":0,"parentEntityLock":"","payAmount":0,"posBillSubDto":{},"printBy":"","printByCd":"","printByUid":"","printDate":"","printWsCd":"","printWsId":0,"profileFlg":"","profileId":0,"profileNo":"","psnNum":0,"reopenBy":"","reopenByCd":"","reopenByUid":"","reopenDate":"","reopenWsCd":"","reopenWsId":0,"resvAreaId":0,"resvCloseDate":"","resvClosePeriod":"","resvNo":"","resvOpenDate":"","resvOpenPeriod":"","roomCd":"","salerBy":"","salerByCd":"","salerByUid":"","salerUnitCd":"","salerUnitUid":"","salesId":0,"seatNo":"","serviceAmount":0,"serviceFlg":"","serviceRate":0,"spareContacterNm":"","spareContacterTlno":"","sysMemo":"","taxAmount":0,"taxCd":"","taxId":0,"taxRate":0,"unitUid":"","unitUidOu":"","version":0,"waiterBy":"","waiterByCd":"","waiterByUid":""},"requestCommonDto":{"sessionKey":"","sysTypeName":"","token":"","tokenStatus":"","tracerId":"","unitUid":"","validReqDtoStatus":""},"submitData":{"acctId":0,"acctNo":"","afterPrintPage":0,"billAmount":0,"billId":0,"billNo":"","billOrigin":"","billOriginNo":"","billStus":"","billTranNo":"","billTyp":0,"blockNum":0,"chainUid":"","closeBy":"","closeByCd":"","closeByUid":"","closeDate":"","closePeriod":"","closeWsCd":"","closeWsId":0,"contacterNm":"","contacterTlno":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","createdWsCd":"","createdWsId":0,"discountAmount":0,"discountFlg":"","discountRate":0,"id":0,"insideBy":"","insideByCd":"","insideByUid":"","insideCd":"","insideDate":"","insideDept":"","insideDeptCd":"","insideDeptUid":0,"insideFlg":"","insideMemo":"","insideUid":0,"insideUnitCd":"","insideUnitUid":0,"makeAmount":0,"makeupFlg":"","marketTyp":0,"memo":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","modifiedWsCd":"","modifiedWsId":0,"openBy":"","openByCd":"","openByUid":"","openDate":"","openFlg":"","openPeriod":"","orgTyp":0,"parentEntityLock":"","payAmount":0,"posBillSubDto":{},"printBy":"","printByCd":"","printByUid":"","printDate":"","printWsCd":"","printWsId":0,"profileFlg":"","profileId":0,"profileNo":"","psnNum":0,"reopenBy":"","reopenByCd":"","reopenByUid":"","reopenDate":"","reopenWsCd":"","reopenWsId":0,"resvAreaId":0,"resvCloseDate":"","resvClosePeriod":"","resvNo":"","resvOpenDate":"","resvOpenPeriod":"","roomCd":"","salerBy":"","salerByCd":"","salerByUid":"","salerUnitCd":"","salerUnitUid":"","salesId":0,"seatNo":"","serviceAmount":0,"serviceFlg":"","serviceRate":0,"spareContacterNm":"","spareContacterTlno":"","sysMemo":"","taxAmount":0,"taxCd":"","taxId":0,"taxRate":0,"unitUid":"","unitUidOu":"","version":0,"waiterBy":"","waiterByCd":"","waiterByUid":""}}
            jsondump_params=json.dumps(params)
            print " @@@@@@@@@@@@@@@@@the requestjson >>>>>>>>>>>>>> ",jsondump_params
            sessionKeyStr=loginSessionKey.getLoginSessionKey()
            print " @@@@@@@@@@@@@@@@@the sessionkey >>>>>>>>>>>>>>",sessionKeyStr
            tokenStr=loginSessionKey.getTokenKey(sessionKeyStr)
            print " @@@@@@@@@@@@@@@@@the tokenStr >>>>>>>>>>>>>>",tokenStr
            headers = {"Content-type": "application/json; charset=UTF-8" , "Accept": "*/*", "jw_data": sessionKeyStr, "jw_token": tokenStr}
            self.httpClient.request("POST", "/3160001RA-1.0.0-SNAPSHOT/bs/PosBill/updatePosBill",jsondump_params, headers)

            #response is HTTPResponse Object
            response = self.httpClient.getresponse()
            print response.reason
            reponstr = response.read()
            responsejsonStr={"responseCommonDto":{"errorLevel":"","lans":"","message":"","resultCode":"","sessionKey":"","token":"","tracerId":""},"resultData":{"acctId":0,"acctNo":"","afterPrintPage":0,"billAmount":0,"billId":0,"billNo":"","billOrigin":"","billOriginNo":"","billStus":"","billTranNo":"","billTyp":0,"blockNum":0,"chainUid":"","closeBy":"","closeByCd":"","closeByUid":"","closeDate":"","closePeriod":"","closeWsCd":"","closeWsId":0,"contacterNm":"","contacterTlno":"","createdBy":"","createdByCd":"","createdByUid":"","createdDate":"","createdUnitCd":"","createdUnitUid":"","createdWsCd":"","createdWsId":0,"discountAmount":0,"discountFlg":"","discountRate":0,"id":0,"insideBy":"","insideByCd":"","insideByUid":"","insideCd":"","insideDate":"","insideDept":"","insideDeptCd":"","insideDeptUid":0,"insideFlg":"","insideMemo":"","insideUid":0,"insideUnitCd":"","insideUnitUid":0,"makeAmount":0,"makeupFlg":"","marketTyp":0,"memo":"","modifiedBy":"","modifiedByCd":"","modifiedByUid":"","modifiedDate":"","modifiedUnitCd":"","modifiedUnitUid":"","modifiedWsCd":"","modifiedWsId":0,"openBy":"","openByCd":"","openByUid":"","openDate":"","openFlg":"","openPeriod":"","orgTyp":0,"parentEntityLock":"","payAmount":0,"posBillSubDto":{},"printBy":"","printByCd":"","printByUid":"","printDate":"","printWsCd":"","printWsId":0,"profileFlg":"","profileId":0,"profileNo":"","psnNum":0,"reopenBy":"","reopenByCd":"","reopenByUid":"","reopenDate":"","reopenWsCd":"","reopenWsId":0,"resvAreaId":0,"resvCloseDate":"","resvClosePeriod":"","resvNo":"","resvOpenDate":"","resvOpenPeriod":"","roomCd":"","salerBy":"","salerByCd":"","salerByUid":"","salerUnitCd":"","salerUnitUid":"","salesId":0,"seatNo":"","serviceAmount":0,"serviceFlg":"","serviceRate":0,"spareContacterNm":"","spareContacterTlno":"","sysMemo":"","taxAmount":0,"taxCd":"","taxId":0,"taxRate":0,"unitUid":"","unitUidOu":"","version":0,"waiterBy":"","waiterByCd":"","waiterByUid":""}}
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

