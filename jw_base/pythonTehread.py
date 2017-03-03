#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月3日

@author: lei.wang
'''

import threading
from time import ctime,sleep

def music(entertainment):
    for i in range(2):
        print "Listening to %s. %s" %(entertainment,ctime())
        sleep(1)


def movie(entertainment):
    for i in range(2):
        print "Watching the %s. %s" %(entertainment,ctime())
        sleep(5)



if __name__ == '__main__':
    threads = []
    thread_music = threading.Thread(target=music,args=(u"暗号",))
    threads.append(thread_music)
    thread_movie = threading.Thread(target=movie,args=(u"肖圣克救赎",))
    threads.append(thread_movie)

    for each in threads:
        each.setDaemon(True)
        each.start()

    each.join()

    print "all threads end at %s" %(ctime())