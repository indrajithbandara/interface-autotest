#!/usr/bin/env python2.7
#coding: utf-8
import os

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
            #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList
import os

def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)
for fullname in iterbrowse("F:\\JDdata\\images\\training"):
    #fullname是绝对路径
    #print fullname
    filename=os.path.basename(fullname)
    #filename是目录下的所有文件名
    print filename
os.system("pause")
list = GetFileList('D:\\workspace\\PyDemo\\fas', [])
for e in list:
    print e

import os

def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)
for fullname in iterbrowse("F:\\JDdata\\images\\training"):
    #fullname是绝对路径
    #print fullname
    filename=os.path.basename(fullname)
    #filename是目录下的所有文件名
    print filename
os.system("pause")