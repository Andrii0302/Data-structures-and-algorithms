class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str (self.value)
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
        if self.length>0:
            result+=' ↺'
        return result

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
    def get(self,index):
        if index == -1:
            return self.tail
        elif index < 0 or index >= self.length:
            return None
        current=self.head
        for _ in range(index):
            current=current.next
        return current #current.value
    # def pop_first(self):
    #     current=self.head
    #     self.head=current.next
    #     self.tail.next=current.next
    #     current.next=None
    #     self.length-=1
    #     return current
    def pop_first(self):
        if self.length == 0:
            return None
        current=self.head
        if self.length == 1:
            self.head=None
            self.tail=None
            return current
        self.head=self.head.next
        self.tail.next=self.head
        current.next=None
        self.length-=1
        return current
    def pop(self):
        popped=self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head=None
            self.tail=None
            self.length=-1
            return popped
        else:
            prev_node=self.head
            while prev_node.next is not self.tail:
                prev_node=prev_node.next
            prev_node.next=self.head
            self.tail=prev_node
            popped=None
            self.length-=1
            return popped
    def clear(self):
        if self.length ==0:
            return 
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0
list1=CSLL()
for i in range(6):
    list1.insert(i*10,i)



print(list1.clear())
print(list1)
        


