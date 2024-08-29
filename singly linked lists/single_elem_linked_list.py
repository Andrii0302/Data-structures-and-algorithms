class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
new_node = Node(10)
# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.lenght=1
# new_linked_list=LinkedList(20)


# empty linked list
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.lenght=0
new_linked_list=LinkedList()
        
print(new_linked_list.lenght)