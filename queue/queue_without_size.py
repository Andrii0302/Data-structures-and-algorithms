class Queue:
    def __init__(self):
        self.items=[]
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    def enqueue(self,value):
        self.items.append(value)
        return 'inserted'
    
    def dequeue(self):
        if self.isEmpty():
            return 'empty'
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return 'empty'
        else:
            return self.items[0]
        
    def delete(self):
        self.items=None
    
queue1=Queue()
print(queue1.isEmpty())
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.dequeue()
print(queue1)
