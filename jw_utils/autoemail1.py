#!/usr/bin/env python2.7
#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'jwlabusertester@163.com'
#receiver = 'jwlabusertester@163.com'
#receiver = 'j_cui@jointwisdom.cn'
receiver = ''
subject = 'ok'
smtpserver = 'smtp.163.com'
username = 'jwlabusertester@163.com'
password = 'Passw0rd'

msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()