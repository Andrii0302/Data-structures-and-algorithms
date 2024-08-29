from random import randint
class Node:
    def __init__(self,value=None):
        self.value=value 
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self,values=None):
        self.head=None
        self.tail=None
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next
    def __str__(self):
        values=[str(x.value) for x in self]
        return ' -> '.join(values)
    def __len__(self):
        result=0
        node=self.head
        while node:
            result+=1
            node=node.next
        return result
    def append(self,value):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return self.tail
    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for i in range(n):
            self.append(randint(min_value,max_value))
        return self
