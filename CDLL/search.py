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
    def search(self, target):
        index=0
        current=self.head
        while current:
            if current.value == target:
                return index
            current=current.next
            index+=1
            if current == self.head: return -1
newCDLL=CDLL()
newCDLL.append(10)
newCDLL.append(20)
newCDLL.append(30)
newCDLL.append(40)
print(newCDLL.search(30))
print(newCDLL)