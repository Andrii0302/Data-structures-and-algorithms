class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
     
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break  # Stop condition for circular list                    
            result += ' -> '
        return result
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
     
    def count(self):
        counter=0
        nod=self.head
        while True:
            counter+=1
            nod=nod.next
            if nod == self.head:
                break
        return counter

