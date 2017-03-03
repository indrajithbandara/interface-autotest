# -*- coding: utf-8 -*-
#encoding:utf-8
class Node():
    data = None
    nextnode = None
    prenode = None
    def __init__(self, data):
        self.data = data
class PersonChan():
    size = 0
    head = None
    tail = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    #增加节点
    def add_node(self, a):
        newnode = Node(a)
        if(self.head == None):
            self.head = newnode
            self.head.prenode = None
            self.tail = newnode
            self.tail.prenode = None
            self.tail.nextnode = None
            self.size = self.size+1
        else:
            temp = self.head
            while temp.nextnode is not None:#返回尾节点tail
                temp = temp.nextnode
            temp.nextnode = newnode
            self.tail = newnode
            self.tail.prenode = temp
            self.tail.nextnode = None
            self.size = self.size+1
    #在查找到的a后面增加节点
    def ins_node(self,a,b):
        newnode = Node(b)
        if self.head ==None:
            self.head = newnode
            self.tail = newnode
            print("Insert success:",newnode.data)
            self.size = self.size +1
        else:
            temp = self.head
            while(temp is not None)&(temp.data != a):
                temp = temp.nextnode
            if temp.nextnode == None:
                temp.nextnode = newnode
                self.tail = newnode
                self.tail.prenode = temp
                self.tail.nextnode = None
                temp = None
                print("Insert success:",newnode.data)
                self.size = self.size+1
            else:
                newnode.prenode = temp
                newnode.nextnode = temp.nextnode
                temp.nextnode = newnode
                print("Insert success:",newnode.data)
                self.size = self.size+1
    #删除节点
    def del_node(self,a):
        if self.head == None:
            pass
        elif self.head.data == a:
            if self.size ==1:
                self.head = None
                self.tail = None
                self.size = self.size-1
            else:
                self.head = self.head.nextnode
                self.size = self.size -1
        else:
            temp = self.head.nextnode
            while (temp is not None) and (temp.data != a):
                temp = temp.nextnode
            p = temp.prenode
            if temp != None:
                if temp.nextnode == None:

                    self.tail = p
                    self.tail.nextnod = None
                else:
                    p.nextnode = temp.nextnode
                    temp = None
                self.size = self.size -1
                print("Delete is success:",a)
    def listall(self):#正序排列
        if self.size == 0:
            print("No data in the list")
        else:
            temp = self.head
            while(temp is not None):
                print(temp.data)
                temp = temp.nextnode
    def lista(self):#倒序排列
        if self.size == 0:
            print("No data in the list")
        temp = self.tail
        while(temp is not None):
            print(temp.data)
            temp = temp.prenode

if __name__ == '__main__':
    link = PersonChan()
    link.add_node(1)
    link.add_node(2)
    link.add_node(3)
    link.add_node(4)
    link.listall()
    print("The list's size is:",link.size)
    link.lista()