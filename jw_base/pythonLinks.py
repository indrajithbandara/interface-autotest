# -*- coding: utf-8 -*-
#encoding:utf-8

class Node:
    next = None
    data = None
    def __init__(self,nodeData):
        self.data = nodeData

class List:
    head = None
    size = 0
    def __init__(self):
        self.size = 0
        self.head = None

    #遍历链表
    def a(self):
        print("avx")
    def printlist(self):
        p=self.head
        while(p is not None):
            print(p.data)
            p=p.next
        print("——————————————————————————————————————")

    def insertlink(self, a, newdata):
        newnode = Node(newdata)
        if self.size == 0:
            print("The link is none")
            self.head = newnode
            self.size = self.size+1
        else:
            p = self.head
            while(p is not None )and (p.data != a):
                p = p.next
            if p.next is None:
                p.next = newnode
                self.size = self.size + 1
            else:
                newnode.next = p.next
                p.next = newnode
                self.size = self.size + 1

    #删除链表中的节点
    def deldata(self,a):
        if self.size == 0:
            print("The link is none")
        elif self.size ==1:
            self.head = None
            self.size = self.size -1
        else:
            p = self.head
            while(p is not None )and (p.data != a):
                q = p
                p = p.next
            if p is None:
                print("Can't find a")
            elif p == self.head:
                self.head = p.next
            elif p.data ==a and p.next is not None:
                q.next = q.next.next
                self.size = self.size - 1
            else:
                q.next = None
                self.size = self.size - 1


    #修改链表中的指定节点
    def updatelink(self,a,b):
        p = self.head
        print(p.data)
        while(p is not None ) and (p.data!=a):
            p = p.next
        if p is None:
            print("Can't find a")
        else:
            p.data = b

if __name__=="__main__":
    p = List()
    p.insertlink(1,1)
    p.insertlink(1,2)
    p.insertlink(1,3)
    p.insertlink(1,4)
    print("_________________________---insertlink")
    p.printlist()
    print("_________________________--chalink")
    p.updatelink(2,5)
    p.printlist()
    print("___________________________-----dellink")
    p.deldata(5)
    p.printlist()