#-*-coding:utf-8-*-
'''
Created on 2016-1-26
updated on 2016-3-16
@author: xuhao
Description:删除指定路径下的目录
'''

#python，用递归删除目录以及下面的文件和文件夹
import os
def removeDir(dirPath):
    if not os.path.isdir(dirPath):
        return
    files = os.listdir(dirPath)
    try:
        for file in files:
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                removeDir(filePath)
        os.rmdir(dirPath)
    except Exception, e:
        print e

#removeDir("c:/ljq/")
