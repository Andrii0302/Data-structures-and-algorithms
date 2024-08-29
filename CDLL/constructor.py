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
# CDLL with 1 element, have to put value while creating a list
# class CDLL:
#     def __init__(self,value):
#         new_node=Node(value)
#         new_node.next=new_node
#         new_node.prev=new_node
#         self.head=new_node
#         self.tail=new_node
#         self.length=1
newCDLL= CDLL()
newCDLL.append(10)
newCDLL.append(20)
print(newCDLL.tail)