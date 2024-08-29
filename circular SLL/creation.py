class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# CSLL with on element
class CSLlist:
    def __init__(self,value):
        new_node=Node(value)
        new_node.next=new_node
        self.head=new_node
        self.tail=new_node
        self.length=1
# empty csll
class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

