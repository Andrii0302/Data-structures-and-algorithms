class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)

class CDLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp_node=self.head
        result='↺ '
        while temp_node:
            result+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node == self.head: break
            result+=' <-> '
        return result +' ↺'
    def append(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
    def prepend(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.prev=self.tail
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def get(self,index):
        if index < 0 or index >=self.length:
            return None
        current=None
        if index < self.length //2:
            current=self.head
            for i in range(index):
                current=current.next
        else:
            current=self.tail
            for i in range(self.length-1,index,-1):
                current=current.prev
        return current
    def insert(self,index,value):
        if index < -1 or index > self.length:
            return
        if index == 0 or self.length == 0:
            self.prepend(value)
            return
        elif index == -1 or index == self.length:
            self.append(value)
            return
        else:
            new_node=Node(value)
            prevv=self.get(index-1)
            new_node.next=prevv.next
            new_node.prev=prevv
            prevv.next.prev=new_node
            prevv.next=new_node
            self.length+=1

newCDLL=CDLL()
newCDLL.append(10)
newCDLL.append(20)
newCDLL.append(30)
newCDLL.append(40)
newCDLL.insert(1,3)
print(newCDLL)