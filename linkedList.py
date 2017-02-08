#!/usr/bin/python2
#usage:
#   import linkedlist
#   l = linkedlist()
#   l.initlist([])
#   l.append("data1")
#   l.insert(1,"data2")
#   l.delete(1)
#   l.index("data1")
#   l[1] = 4


class Node(object):
    #basic node
    def __init__(self, val, p=0):
        #next is defaultly point to 0
        self.data = val
        self.next = p

class LinkedList(object):
    def __init__(self):
        self.head = 0

    def init_list(self, data):
        #remark! self.head is a Node type now!!
        #to init a linkedlist, there must be a value in the list.
        self.head = Node(data[0])
        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def get_length(self):
        length = 0
        p = self.head
        while p != 0:
            length += 1
            p = p.next

        return length

    def is_empty(self):
        #or self.head == 0
        if self.get_length() == 0:
            return True

        else:
            return False 

    def append(self,item):
        p = self.head

        while p.next != 0:
            p = p.next

        node = Node(item)
        p.next = node

    def get_item(self,index):
        if self.is_empty():
            print("This linked list is empty.\n")
            return 

        i = 0
        p = self.head

        while p.next != 0 and i < index:
            i += 1
            p = p.next

        if i == index:
            return p.data

        else:
            print("target item is not exist.\n")


    def get_index(self, item):
        p = self.head
        i = 0
        index_pool = []

        if self.is_empty():
            print("no node in the linked list\n")
            return 

        while p != 0:
            if p.data == item:
                index_pool.append(i)

            p = p.next
            i += 1

        return index_pool


    def insert(self, index, item):
        p = self.head
        post = self.head
        i = 0

        if index == 0:
            node = Node(item, self.head)
            self.head = node
            return True

        while p.next != 0 and i < index:
            i += 1
            post = p
            p = p.next

            if index == i:
                node = Node(item)
                post.next = node
                node.next = p
                return True


    def delete(self, index):
        p = self.head
        post = self.head
        i = 0

        if self.is_empty():
            print ("no node in the linked list to delete\n")
            return False

        if index == 0:
            self.head = p.next
            p = 0
            return True

        while p.next != 0 and i < index:
            i += 1
            post = p
            p = p.next

            if i == index:
                post.next = p.next
                p = 0
                return True


    def traverse(self):
        p = self.head
        while p!= 0:
            print ("%s " % p.data)
            p = p.next


