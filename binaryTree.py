#!/usr/bin/python2
#usage:
#   import binarytree
#   b = binarytree.Binarytree(5)
#   b.append(4)
#   b.append(8)
#       5
#      / \
#     4   8
#    /   / \
#   3   7   9
#
#   b.delete(4)
#   b.dfs(7)
#   b.bfs(8)
import stack
import queue


class Node(object):
    def __init__(self, root=None, left=None, right=None):
        self.root_val = root
        self.left = left
        self.right = right


class Binarytree(object):
    def __init__(self, top_root=None):
        self.top_root = Node(top_root)
        self.traveral = []


    def append(self, item, root=None):
        if root == None:
            root = self.top_root

        if item == root.root_val:
            return False

        else:
            if item > root.root_val:
                if root.right != None:
                    return self.append(item, root.right)

                elif root.right == None:
                    node = Node(item)
                    root.right = node
                    return True

                else:
                    return False

            elif item < root.root_val:
                if root.left != None:
                    return self.append(item, root.left)

                elif root.left == None:
                    node = Node(item)
                    root.left = node
                    return True

                else:
                    return False


    def delete(self, item):
        pass 

    def dfs(self, root=None):
        if root == None:
            root = self.top_root

        s = stack.Stack()
        s.push(root)

        while s.top > 0:
            root = s.pop()
            self.traveral.append(root.root_val)

            if root.right!= None:
                s.push(root.right)
            if root.left != None:
                s.push(root.left)


    def bfs(self, root=None):
        if root == None:
            root = self.top_root

        q = queue.Queue()        
        q.enqueue(self.top_root)

        while not q.is_empty():
            root = q.dequeue()
            self.traveral.append(root.root_val)

            if root.left != None:
                q.enqueue(root.left)
            if root.right != None:
                q.enqueue(root.right)


    def preorder(self, root=None):
        if root == None: 
            root = self.top_root

        self.traveral.append(root.root_val)
        if root.left != None: 
            self.preorder(root.left)
        if root.right != None:
            self.preorder(root.right)


    def inorder(self, root=None):
        if root == None:
            root = self.top_root

        if root.left != None: 
            self.inorder(root.left)
        self.traveral.append(root.root_val)
        if root.right != None:
            self.inorder(root.right)


    def postorder(self, root=None):
        if root == None:
            root = self.top_root

        if root.left != None: 
            self.postorder(root.left)
        if root.right != None:
            self.postorder(root.right)
        self.traveral.append(root.root_val)
