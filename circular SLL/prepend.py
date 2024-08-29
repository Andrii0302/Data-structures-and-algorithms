class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# CSLL with on element
class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=Node(value)
        if self.length ==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node #reference to itself
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1

    def prepand(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node #moves head pointer
            self.tail.next=new_node # creates link from tail to head
        self.length+=1
list1=CSLL()
list1.append(10)
list1.append(20)
list1.append(30)
print(list1)
        


