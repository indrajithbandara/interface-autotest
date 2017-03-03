# -*- coding: utf-8 -*-
#encoding:utf-8
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
import unittest, time, re
import HTMLTestRunner,sys
import generateCode
import os
import shutil
#sys.path.append('c:\\mypythonlib')
sys.path.append("../")
sys.path.append("../jw_utils")
sys.path.append("../jw_base")
from jw_utils import connection_postdb
from jw_utils.logUtils import *
from jw_utils import pythonEmail
import httplib, urllib,json

#excute automation http reqyest
#http://www.yiibai.com/html/postgresql/2013/080998.html
if __name__ == '__main__':
    suite = unittest.TestSuite()
    filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='../test-log/'+filename+'.log',
                    filemode='w')
    ###########################################################################################################
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')
    #windows dir path
    import ConfigParser
    config=ConfigParser.ConfigParser()
    with open('../test-config/systemcfg.properties', 'r') as cfg:
        config.readfp(cfg)
        # print config.get('config', 'username')
        logging.info(config.get('config', 'testsuit_dir'))
        testsuit_dir=config.get('config', 'testsuit_dir')
        logging.info(config.get('config', 'testsuit_report_dir'))
        testsuit_report_dir=config.get('config', 'testsuit_report_dir')
        print "@@@@@@@@@@jw-interface-reqip@@@@@@@@@@@",config.get('config', 'jw-interface-reqip')
        jw_interface_reqip=config.get('config', 'jw-interface-reqip')
        print "@@@@@@@@@@jw-interface-reqport@@@@@@@@@@@",config.get('config', 'jw-interface-reqport')
        jw_interface_reqport=config.get('config', 'jw-interface-reqport')
        count_result=connection_postdb.getIFD_INTERFACEDEF_Count()
        print " the count_result is >>>>>>>>>>>>>>",count_result
    #connect db, and conb the python interface class
    interdef_result=connection_postdb.getIFD_INTERFACEDEF_All()
    print " the interdef table data >>>>>>>>>>>>>>>>",interdef_result
    for inter_row in interdef_result:
        logging.info("===========all interface api iterator　${inter_row} row[3]==============")
        print " the inter_row[13]  is >>>>>>>>> ",inter_row[13]
        print " the inter_row[12]  is >>>>>>>>> ",inter_row[12]
        print " the inter_row[3]  is >>>>>>>>> ",inter_row[3]
        print " the inter_row[6]  is >>>>>>>>> ",inter_row[6]
        print " the inter_row[7]  is >>>>>>>>> ",inter_row[7]
        print " the inter_row[5]  is >>>>>>>>> ",inter_row[5]
        requestjson =inter_row[12].replace('\n','').replace('\r','').replace('null','""').replace('true','""').replace('false','""')
        responsejson =inter_row[13].replace('\n','').replace('\r','').replace('null','""').replace('true','""').replace('false','""')
        inter_name =inter_row[6].replace('\n','').replace('\r','')
        inter_url = inter_row[5].replace('\n','').replace('\r','')
        inter_type = inter_row[7].replace('\n','').replace('\r','')
        inter_chinaname= inter_row[3].replace('\n','').replace('\r','')
        # result_case=connection_postdb.getIFD_EXAMPLEDEF_From_IFD_INTERFACEDEF("infnm1")
        #generate some automation http request api codes
        # print " the result_input is ===>",result_input[3]," the result_output is ===>",result_output[2]," the result_assert is ===>",result_assert[3]
        # print "==@@@@@@@@@@@@@@@@@==%s",result_input[3]
        generateCode.httpPostApiMethod(inter_name,inter_url,requestjson,responsejson,inter_type,jw_interface_reqip,jw_interface_reqport,inter_chinaname)
    # package_name=inter_row[11]
    # strdemo_infcls=package_name[::-1][0:package_name[::-1].find(".")]
    # finalstrdemo_infcls=strdemo_infcls[::-1]
    ###########################################################################################################
    test_dir=os.path.join(os.path.dirname(os.getcwd()),"jw_testcase")
    #test_report_dir=os.path.join(os.path.dirname(os.getcwd()),"test-report").replace('\\','//')
    jwbase_test_report_dir=os.path.join(os.path.dirname(os.getcwd()),"test-report","jwbase_interface_test_report.html")
    # print "===os.getcwd()===>",test_dir,"===　lat jwpms_test_report_dir dir path　os.getcwd()===>",jwpms_test_report_dir.replace('\\','//')
    print os.path.abspath(os.path.dirname(__file__))
    # test_report_dir="/var/lib/jenkins/workspace/test-Python/test-report/"
    #base test report
    ###########################################################################################################
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_*Impl.py')
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print "the current date time is ",currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    nowtime = time.strftime('%Y-%m-%d_%H_%M_%S_')
    # fp = file(test_report_dir+"cwapi"+nowtime+"_test_report.html", 'wb')
    fp = file(jwbase_test_report_dir, 'wb')
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'JW_CloudWisdom_InterfaceAPI_TestReport',description=u"众荟慧云接口用例执行情况 by 201702 softwareluke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    htmlRunner.run(discover)
    fp.close()
    #pythonEmail.send_mail("jwbase_interface_test_report")
    logging.info("the all base interface testing has been done, the email test report sent. ")
    # ###########################################################################################################
    # #eshop test report
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='*shop_*Impl.py')
    # currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # print "the current date time is ",currenttime
    # #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    # nowtime = time.strftime('%Y-%m-%d_%H_%M_%S_')
    # # fp = file(test_report_dir+"cwapi"+nowtime+"_test_report.html", 'wb')
    # fp = file(jwshop_test_report_dir, 'wb')
    # htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'JW_CloudWisdom_Eshop_Interface_TestReport',description=u"用例执行情况 by 201612 softwareluke")
    # #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    # htmlRunner.run(discover)
    # fp.close()
    # pythonEmail.send_mail("jwshop_interface_test_report")
    # logging.info("the all eshop interface testing has been done, the email test report sent. ")
    # ###########################################################################################################
    # #pms test report
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='*pms_*Impl.py')
    # currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # print "the current date time is ",currenttime
    # #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    # nowtime = time.strftime('%Y-%m-%d_%H_%M_%S_')
    # # fp = file(test_report_dir+"cwapi"+nowtime+"_test_report.html", 'wb')
    # fp = file(jwpms_test_report_dir, 'wb')
    # htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'JW_CloudWisdom_EPms_Interface_TestReport',description=u"用例执行情况 by 201612 softwareluke")
    # #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    # htmlRunner.run(discover)
    # fp.close()
    # pythonEmail.send_mail("jwpms_interface_test_report")
    # logging.info("the all pms interface testing has been done, the email test report sent. ")
