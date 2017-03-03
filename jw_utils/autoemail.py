#!/usr/bin/env python2.7
#coding: utf-8
import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# sender = '***'
# receiver = '***'
# subject = 'python email test'
# smtpserver = 'smtp.163.com'
# username = '***'
# password = '***'

sender = 'jwlabusertester@163.com'
#receiver = 'jwlabusertester@163.com'
#receiver = 'j_cui@jointwisdom.cn'
receiver = 'hpecuijun@126.com'
subject = 'jw interface testing python email test report'
smtpserver = 'smtp.163.com'
username = 'jwlabusertester@163.com'
password = 'Passw0rd'


msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
test_report_dir='D:\\Devops-cw.txt'
#构造附件
att = MIMEText(open(test_report_dir, 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename=Devops-cw.txt'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()