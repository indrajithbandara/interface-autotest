# coding:utf-8
'''
Created on 2016-1-26
updated on 2016-3-16
@author: xuhao
Description:report文件夹重命名
'''

import os,time

def re_name():
    #if os.path.exists(r"F:\\Monitor_New\\report"):
    if os.path.exists(r"../report"):
        #获取当前目录
        #os.getcwd()
        #改变工作目录
        #os.chdir('F:\\Monitor_New')
        os.chdir('../')
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        #print now
        #os.close("../report")
        try:
            os.rename("report", "report"+now)
            #os.mkdir("F:\\Monitor_New\\report")
            os.mkdir("report")
        except WindowsError:
            pass
    
if __name__ == '__main__':  
    re_name()
