# -*- coding: UTF-8 -*-
import os
def getFileStr(level):
    return '  '*level+'- '
def getDicStr(level):
    return '  '*level+'+'

def printFile(path,level):
    if os.path.exists(path):
        files = os.listdir(path)
        for f in files :
            subpath=os.path.join(path,f)
           #print(os.path.isfile(subpath))
            if os.path.isfile(subpath):
                print(getFileStr(level)+os.path.basename(subpath))
            else:
                leveli=level+1
                print(getDicStr(level)+os.path.basename(subpath))
                printFile(subpath,leveli)

if __name__=='__main__':
    printFile(r'D:\\PycharmProjects\\cloudwisdom_automation\\jw_utils',1)
    #最后，部分结果如下：