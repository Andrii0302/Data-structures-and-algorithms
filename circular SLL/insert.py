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
    def __str__(self):
        temp_node = self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node == self.head:
                break
            result+=' -> '
        return result+' ↺'
    
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
    def insert(self,value,index):
        new_node=Node(value)
        if index >self.length or index < 0:
            raise Exception ("Index out of range")
        if index == 0:
            if self.length == 0:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            else:
                #list1.prepand(value)
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
        elif index == self.length:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
list1=CSLL()
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.insert(50,4)
print(list1)
        


