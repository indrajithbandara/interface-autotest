#!/usr/bin/env python2.7
#coding: utf-8
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
import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#http://www.cnblogs.com/apexchu/p/4209742.html
#http://www.cnblogs.com/yangxia-test/category/431240.html

def send_mail(report_name):
    sender = 'jwlabusertester@163.com'
    #receiver = 'jwlabusertester@163.com'
    #receiver = 'j_cui@jointwisdom.cn'
    receiver = "3089621191@qq.com,jwlabusertester@163.com"
    subject = 'jw interface testing python email test report'
    smtpserver = 'smtp.163.com'
    username = 'jwlabusertester@163.com'
    password = 'Passw0rd'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message automation testing myemail by softwareluke'
    import ConfigParser
    config=ConfigParser.ConfigParser()
    with open('../test-config/systemcfg.properties', 'r') as cfg:
          config.readfp(cfg)
          # print config.get('config', 'username')
          print config.get('config', 'test_report_dir')
          vartest_report_dir=config.get('config', 'test_report_dir')
    print " the test report name is ======>",report_name
    #构造附件
    # test_report_dir='/var/lib/jenkins/workspace/test-Python/test-report/jwinterface_test_report.html'
    #test_report_dir=vartest_report_dir
    #test_report_dir=os.path.join(os.path.dirname(os.getcwd()),"test-report","jwinterface_test_report.html").replace('\\','//')
    test_report_dir=os.path.join(os.path.dirname(os.getcwd()),"test-report",report_name+".html")
    # test_report_dir='E:\\IDEidea\\IdeaProjects\\jw-automation\\test-report\\jwinterface_test_report.html'
    #'E:\\IDEidea\\IdeaProjects\\jw-automation\\test-report\\cwapi2016-11-10_12_28_34__test_report.html'
    print " the test_report_dir is ",test_report_dir
    att = MIMEText(open(test_report_dir, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename='+report_name+'.html"'
    msgRoot.attach(att)
    try:
       smtp = smtplib.SMTP()
       smtp.connect('smtp.163.com')
       smtp.login(username, password)
       smtp.sendmail(sender, receiver, msgRoot.as_string())
       smtp.quit()
       print "send email is successful............."
       return True
    except Exception, e:
        #print str(e)
        return False


if __name__ == '__main__':
    send_mail()
