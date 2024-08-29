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
    def search_node(self,target):
        current=self.head
        index=0
        while current :
            if current.value==target:
                return index
            current=current.next
            index+=1
        return False

new_linked_list1 = LinkedList()
new_linked_list1.insert(0, 10)
new_linked_list1.insert(1, 20)
new_linked_list1.insert(2, 30)
new_linked_list1.insert(3, 40)
new_linked_list1.insert(4, 50)
new_linked_list1.insert(5, 60)
print(new_linked_list1.search_node(40))
print(new_linked_list1)
