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
            if temp_node == self.head:  # Stop condition for circular list
                break
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
    
    def delete_by_value(self, value):
        if self.length == 0:  # If the list is empty
            return False
 
        # Handle the case where the list has only one node
        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True
 
        prev = None
        current = self.head
        while True:
            if current.value == value:  # Node to delete is found
                if current == self.head:  # Node is at the head
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current == self.tail:  # Node is at the tail
                        self.tail = prev
                
                self.length -= 1
                return True
 
            prev = current
            current = current.next
            if current == self.head:  # If we have traversed the entire list
                break
 
        return False
    
