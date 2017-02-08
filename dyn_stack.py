from linkedlist import *

class Stack(LinkedList):
    def __init__(self, data=[0]):
        LinkedList.__init__(self)
        self.top = self.get_length()
        self.init_list(data)


    def push(self, item):   
        self.append(item)
        self.top += 1


    def pop(self):  
        if self.top < 0:
            print ("no element to pop\n")
            return 

        else:
            p = self.head

            while p.next != 0:
                p = p.next
            pop_val = p.data

            self.delete(self.get_length()-1)
            self.top -= 1

            return pop_val


    def peek(self):
        p = self.head

        while p.next != 0:
            p = p.next

        return p.data
