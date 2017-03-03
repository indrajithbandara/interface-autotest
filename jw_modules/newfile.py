# coding:utf-8
'''
Created on 2016-1-26
updated on 2016-3-16
@author: xuhao
Description:获取指定目录下的最新文件
'''
import os,datetime,time

def new_file():
    result_dir = '..\\report'

    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    if len(lists)>1:
        #print ('最新的文件为： '+lists[-1])
        #print (u'上一次测试生成的报告： '+lists[-2])
        file = os.path.join(result_dir,lists[-1])
        #找到上一次测试生成的文件
        file_new = os.path.join(result_dir,lists[-2])
        #print file_new
        #获取文件修改时间
        data1 = os.stat(file_new).st_mtime
        #获取时间字符串前9位
        time1 =str(data1)[:9]
        #print time1
        #print file
        data2 = os.stat(file).st_mtime
        time2 =str(data2)[:9]
        #print time2
        if time1 == time2:
            #print type([lists[-1],lists[-2]][0])
            #返回列表类型
            filename = [lists[-1],lists[-2]]
            print 11
            print filename
            filepath = [file,file_new]
            print filepath
            return filename
        else:
            filename = [lists[-1]]
            print 22
            print filename
            filepath = file
            print filepath
            return filename
    else:
##        pass
        filename = [lists[-1]]
        print 33
        print filename
        return filename
        
    
if __name__ == '__main__':  
    new_file()

