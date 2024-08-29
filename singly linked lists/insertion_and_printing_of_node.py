class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.lenght=0
        
    def __str__(self):
        temp_node = self.head
        result=''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result+= ' -> '
            temp_node=temp_node.next
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # setting the next attribute of the current tail node to point to the new node being appended. 
            self.tail = new_node
        self.lenght +=1

new_linked_list= LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list)