class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            if index == self.length:
                self.tail = new_node
        self.length += 1
        return True

    def pop_last(self):
        popped_node=self.tail
        if self.length ==0:
            return None
        if self.length ==1:
            self.head= None
            self.tail = None
            return popped_node.value  
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail=temp
            temp.next= None
            self.length -=1
            return popped_node.value
            
new_linked_list1 = LinkedList()
for i in range(6):
    new_linked_list1.insert(i, i*10)
print(new_linked_list1.pop_last())
print(new_linked_list1)
