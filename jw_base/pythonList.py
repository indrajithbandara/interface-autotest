#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月9日

@author: lei.wang
'''

def diff(listA,listB):
    #求交集的两种方式
    retA = [i for i in listA if i in listB]
    retB = list(set(listA).intersection(set(listB)))

    print "retA is: ",retA
    print "retB is: ",retB

    #求并集
    retC = list(set(listA).union(set(listB)))
    print "retC1 is: ",retC

    #求差集，在B中但不在A中
    retD = list(set(listB).difference(set(listA)))
    print "retD is: ",retD

    retE = [i for i in listB if i not in listA]
    print "retE is: ",retE

def main():
    listA = [1,2,3,4,5]
    listB = [3,4,5,6,7]
    diff(listA,listB)

if __name__ == '__main__':
    main()


def nested_list(list_raw,result):
    for item in list_raw:
        if isinstance(item, list):
            nested_list(item,result)
        else:
            result.append(item)

    return  result

def flatten_list(nested):
    if isinstance(nested, list):
        for sublist in nested:
            for item in flatten_list(sublist):
                yield item
    else:
        yield nested

def main():
    list_raw = ["a",["b","c",["d"]]]
    result = []
    print "nested_list is:  ",nested_list(list_raw,result)
    print "flatten_list is: ",list(flatten_list(list_raw))

main()

def dup_remove(list_raw,result):
    for item in list_raw:
        if isinstance(item, list):
            dup_remove(item,result)
        else:
            result.add(item)

    return  list(result)

def main():
    list_raw = ["a",["b","c",["d","a","b"]]]
    result = set()
    print "dup_remove is:  ",dup_remove(list_raw,result)
main()

class Fibonacci(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a,self.b = self.b,self.a + self.b
        print self.a
        return self.a

    def __iter__(self):
        return self

if __name__ == '__main__':
    fib = Fibonacci()
    for n in fib:
        if n > 10:
            #print n
            break


import re

#匹配电话号码
def match_phone_num():
    phone_num = re.compile("0\d{2}-\d{8}|0\d{3}-\d{7}")
    search = phone_num.search("010-123456789")
    if search:
        print search.group()

#匹配ip
def match_ip():
    ip = re.compile("((?P<ThreeNum>2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)")
    search = ip.search("192.168.123.125aaa")
    if search:
        print search.group()

match_ip()