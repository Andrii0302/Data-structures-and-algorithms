class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+=' <-> '
            temp_node=temp_node.next
        return result

    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    def prepand(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
    def get(self,index):
        if index < 0 or index >=self.length:
            return None
        if index < self.length // 2 :
            current=self.head
            for _ in range(index):
                current=current.next
        else:
            current=self.tail
            for _ in range(self.length-1,index,-1):
                current=current.prev
        return current
    def insert(self,index,value):
        new_node=Node(value)
        if index < 0 or index > self.length:
            print("Out of bounds")
            return
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return
        else:
            if index ==0:
                self.prepand(value)
                return
            elif index ==-1:
                self.append(value)
                return
            else:
                temp_node=self.get(index-1)
                new_node.next=temp_node.next
                new_node.prev=temp_node
                temp_node.next.prev=new_node
                temp_node.next=new_node
                self.length+=1
newDLL= DLL()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
newDLL.insert(3,90)
print(newDLL)
