#!/usr/bin/python
# -*- coding: utf-8 -*-
#方法1：使用 in 方法实现contains的功能：
site = 'http://www.jb51.net/'
if "jb51" in site:
    print('site contains jb51')
#输出结果：site contains jb51
#方法2：使用find函数实现contains的功能

s = "This be a string"
if s.find("is") == -1:
    print "No 'is' here!"
else:
    print "Found 'is' in the string."



list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]


list1 = ['physics', 'chemistry', 1997, 2000];
print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
del dict ;        # 删除词典

print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];
#但这会引发一个异常，因为用del后字典不再存在：
# dict['Age']:
#Traceback (most recent call last):
#  File "test.py", line 8, in <module>
#    print "dict['Age']: ", dict['Age'];
#TypeError: 'type' object is unsubscriptable

# from datetime import datetime
#
# class MyFile():
#
#     def __init__(self, filepath):
#         print('MyFile init...')
#         self.filepath = filepath
#
#     def printFilePath(self):
#         print(self.filepath)
#
#     def testReadFile(self):
#         with open(self.filepath, 'r') as f:
#             s = f.read()
#             print('open for read...')
#             print(s)
#
#     def testWriteFile(self):
#         with open('test.txt', 'w') as f:
#             f.write('今天是 ')
#             f.write(datetime.now().strftime('%Y-%m-%d'))





