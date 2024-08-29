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
    def pop_first(self):
        remove=self.head
        if self.length ==0:
            return None
        if self.length == 1:
            self.head=None
            self.tail=None
            self.length=0
            return remove
        else:
        
            self.head=self.head.next
            self.head.prev=None
            remove.next=None
            self.length-=1
            return remove
newDLL= DLL()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
print(newDLL.pop_first())
print(newDLL)
