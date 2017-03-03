def print_List(list_nums):
    for each_item in list_nums :
        if isinstance(each_item,list):
            print_List(each_item)
        else:
            print(each_item)
movies = ["aaa","bbb","ccc","ddd",["qqq","sss",["mmm","rrr",["tt","ccs"]]]]
print_List(movies)


# -*- coding: utf-8 -*-
#!/usr/bin/python
#Filename:copyfile.py
import os,shutil
def mycopy(srcpath,dstpath):
if not os.path.exists(srcpath):
print "srcpath not exist!"
if not os.path.exists(dstpath):
print "dstpath not exist!"
for root,dirs,files in os.walk(srcpath,True):
for eachfile in files:
shutil.copy(os.path.join(root,eachfile),dstpath)
srcpath='e:\\pic'
dstpath='f:\\pictotal'
mycopy(srcpath,dstpath)


import copy

def combine(l, n):
    answers = []
    one = [0] * n
    def next_c(li = 0, ni = 0):
        if ni == n:
            answers.append(copy.copy(one))
            return
        for lj in xrange(li, len(l)):
            one[ni] = l[lj]
            next_c(lj + 1, ni + 1)
    next_c()
    return answers

print combine([1, 2, 3, 4, 5], 3)
