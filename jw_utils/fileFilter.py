# coding:utf-8
'''
Created on 2016-1-26
updated on 2016-3-16
@author: xuhao
Description:获取指定目录下的图片文件
'''

import os,datetime,time

def endWith(s,*endstring):
    array = map(s.endswith,endstring)
    if True in array:
            return True
    else:
            return False
 
def imgFile():
    s = os.listdir('..\\report')
    print s
    f_file = []
    for i in s:
        if endWith(i,'.png','.jpg'):
            f_file.append(i)
            #print f_file
            #return i
    print f_file
    return f_file
if __name__ == '__main__':
    imgFile()
