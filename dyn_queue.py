from linkedlist import *

class Queue(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        self.init_list(data = [0])

        self.qhead = 0
        self.qtail = 0

        self.qt_post = self.qhead

    def is_empty(self):
        if self.qhead == self.qtail:
            return True
        else:
            return False

    def get_qt_post(self):
        p = self.qhead
        while p.next != 0:
            p =  p.next

        self.qt_post = p

    def enqueue(self, item):

        if self.is_empty():
            self.qhead = self.head
            self.qhead.data = item

        else:
            self.get_qt_post()

            node = Node(item)

            self.qt_post.next = node
            node.next = self.qtail


    def dequeue(self):
        #qwhen qhead.next == qtail, queue empty
        if self.is_empty():
            print("the queue is empty, no element to dequeue\n")
            return 

        else:
            dequeue_val = self.qhead.data
            self.qhead = self.qhead.next
            return dequeue_val
