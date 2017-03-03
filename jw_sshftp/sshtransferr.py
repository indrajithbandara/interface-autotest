#!/usr/bin/env python
#coding:utf-8
#http://www.cnblogs.com/wupeiqi/articles/5501365.html
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.18.214', 22, 'root', 'eNw6Luth')
stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()
stdin, stdout, stderr = ssh.exec_command('ps -elf|grep tomcat')
print stdout.read()
stdin, stdout, stderr = ssh.exec_command('netstat -ntlp')
print stdout.read()
ssh.close();

import time
print time.time()
print time.mktime(time.localtime())

print time.gmtime()    #可加时间戳参数
print time.localtime() #可加时间戳参数
print time.strptime('2014-11-11', '%Y-%m-%d')

print time.strftime('%Y-%m-%d') #默认当前时间
print time.strftime('%Y-%m-%d',time.localtime()) #默认当前时间
print time.asctime()
print time.asctime(time.localtime())
print time.ctime(time.time())

import datetime
'''
datetime.date：表示日期的类。常用的属性有year, month, day
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond
datetime.datetime：表示日期时间
datetime.timedelta：表示时间间隔，即两个时间点之间的长度
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
strftime("%Y-%m-%d")
'''
import datetime
print datetime.datetime.now()
print datetime.datetime.now() - datetime.timedelta(days=5)