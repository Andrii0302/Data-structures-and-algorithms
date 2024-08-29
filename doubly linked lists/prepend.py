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
newDLL= DLL()
newDLL.prepand(10)
newDLL.prepand(20)
newDLL.prepand(30)
newDLL.prepand(40)
print(newDLL)