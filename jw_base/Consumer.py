#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import time
import threading
import Queue
import urllib2

class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue=queue

    def run(self):
        while True:
            content =self._queue.get()
            if isinstance(content,str) and content == 'quit':
                break
            response =urllib2.urlopen(content)
        print 'Bye Byes'

def Producer():
    urls = [
         'http://wwww.python.org','http://wwww.yahoo.org'
         'http://wwww.scale.org','http://wwww.golang.org'
    ]
    queue =Queue.Queue()
    work_threads =build_worker_pool(queue ,4)
    start_time =time.time()

    for ur in urls:
        queue.put(url)
    for worker i work_threads:
        queue.put('quit')
    for worker in work_threads:
        worker.join()


def build_worker_pool(queue,size):
    workers = []
    for _ in range(size):
        worker =Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers

if __name__ == '__main__':
    Producer()
