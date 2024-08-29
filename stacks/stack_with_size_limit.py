class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list=[]

    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull():
            return 'Stack is full'
        else:
            self.list.append(value)
            return 'Inserted'
        
    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
            return self.list[-1]
    
    def delete(self):
        self.list=None
        
stack1=Stack(4)
print(stack1.isEmpty())
print(stack1.isFull())
stack1.push(10)
stack1.push(20)
stack1.push(30)
print(stack1)