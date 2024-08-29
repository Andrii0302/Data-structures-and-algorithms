class Queue:
    def __init__(self,maxSize):
        self.items=maxSize * [None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1
    
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top ==-1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            return 'Full'
        else:
            if self.top + 1 ==self.maxSize:
                self.top=0
            else:
                self.top +=1
                if self.start == -1:
                    self.start=0
            self.items[self.top]=value
            return 'inserted'
    def dequeue(self):
        if self.isEmpty():
            return 'empty'
        else:
            first=self.items[self.start]
            start=self.start
            if self.start == self.top:
                self.start =-1
                self.top =-1
            elif self.start + 1 == self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return first
    def peek(self):
        if self.isEmpty():
            return 'empty'
        else:
            return self.items[self.start]
    def delete(self):
        self.items=self.maxSize *[None]
        self.top=-1
        self.start=-1
        
queue1=Queue(3)
print(queue1.isEmpty())
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.dequeue()
print(queue1)