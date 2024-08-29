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
    def pop_first(self):
        popped=self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            popped.prev=None
            popped.next=None
            self.head.prev=self.tail
            self.tail.next=self.head
        self.length-=1
        return popped
    def pop(self):
        if self.length == 0:
            return None
        popped=self.tail
        if self.length == 1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            popped.next=None
            popped.prev=None
            self.tail.next=self.head
            self.head.prev=self.tail
        self.length-=1
        return popped
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
    def remove(self,index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == -1 or index == self.length-1:
            self.pop()
        else:
            popped=self.get(index)
            popped.prev.next=popped.next
            popped.next.prev=popped.prev
            popped.next=None
            popped.prev=None
            self.length-=1
            return popped


newCDLL=CDLL()
newCDLL.append(10)
newCDLL.append(20)
newCDLL.append(30)
newCDLL.append(40)
newCDLL.remove(0)
print(newCDLL)