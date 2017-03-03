#!/usr/bin/python
# coding:utf8
/*
Copyright 2016 JointWisdom Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
import os


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile


test_dir = "D:\\PycharmProjects\\cloudwisdom_automation\\jw_utils"
#print dirlist("/home/yuan/testdir", [])
print dirlist(test_dir, [])


import os
import sys
import os.path
dirroot = "D:\\PycharmProjects\\cloudwisdom_automation\\jw_utils"
line_num = 0
#parent是父文件夹;dirnames是dirroot所含文件夹;
for parent,dirnames,filenames in os.walk(dirroot):
    print ("进入文件夹:" + dirroot)
    for filename in filenames:
        file = dirroot + filename
        print ("读取" + file)
        fin = open(file,'r')
        for lines in fin:
            line_num += 1
            if line_num % 10000 == 0:
               print line_num
        fin.close()
file_destin = dirroot + "line_num.txt"
fout = open(file_destin,'w')
fout.write("文件数" + '\t' + line_num)
fout.close()

# !user/bin/python
fr = open('aa.txt', 'r')
fw = open('b.txt', 'w+')

def restr(s):  # 递归实现函数
    str1 = s.readline()
    if len(str1) != 0:
        restr(s)
    fw.write(str1)

restr(fr)
fr.close()
fw.close()

# !/user/bin/python
# !conding=utf8

import os

g = os.walk("/home/yuan/testdir")

for path, d, filelist in g:
    print d;
    for filename in filelist:
        print os.path.join(path, filename)
