class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()

    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue(self,value):
        new=Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head=new
            self.linkedlist.tail=new
        else:
            self.linkedlist.tail.next=new
            self.linkedlist.tail=new

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.linkedlist.head == None:
            return 'empty'
        else:
            tempnode=self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head= None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head= self.linkedlist.head.next
            return tempnode
    def peek(self):
        if self.isEmpty():
            return 'empty'
        else:
            return self.linkedlist.head
        
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None
queue1=Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.dequeue()
print(queue1)

