#!/usr/bin/env python2.7
#coding: utf-8
import os

dir = r'D:\ecliworkspace'
specify_str = 'm'

# 搜索指定目录
results = []
folders = [dir]

for folder in folders :
    # 把目录下所有文件夹存入待遍历的folders
    folders += [os.path.join(folder, x) for x in os.listdir(folder)
                if os.path.isdir(os.path.join(folder, x))]

    # 把所有满足条件的文件的相对地址存入结果results
    results += [os.path.relpath(os.path.join(folder, x), start = dir)
                for x in os.listdir(folder)
                if os.path.isfile(os.path.join(folder, x)) and specify_str in x]

# 输出结果
for result in results:
    print(result)
print('找到 %s 个结果！' % len(results))