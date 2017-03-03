#coding:utf-8
'''
Created on 2016-1-26
updated on 2016-3-16
@author: xuhao
Description:环境初始化，删除所有report目录，重新创建一个空report目录
'''

import glob,os
from delete_dir import removeDir

def del_rep():
    #不包含子目录的遍历 
    for filename in glob.glob("F:\\Monitor_New\\repor*"):
        print filename
        removeDir(filename)
    #判断某路径下文件是否存在
    value = os.path.exists(r'../report')
    if value == False:
        os.chdir('../')
        os.mkdir("report")    

'''
import os
import fnmatch
 
def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)
            
#查找f:/py及其子目录中的”*.exe" 函数iterfindfile的第一个参数是开始查找的路径，第二个参数是文件名通配表达式
for filename in iterfindfiles(r"f:/py", "*.exe"):
    print filename

'''

if __name__ == "__main__":
    del_rep()
