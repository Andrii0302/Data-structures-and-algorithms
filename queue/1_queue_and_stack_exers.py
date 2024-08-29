class MultiStack:
    def __init__(self,stackSize):
        self.numberstacks=3
        self.cutlist=[0]*(stackSize * self.numberstacks)
        self.size=[0] * self.numberstacks
        self.stackSize= stackSize
    
    def isFull(self,stacknum):
        if self.size[stacknum] == self.stackSize:
            return True
        else:
            return False
    
    def isEmpty(self,stacknum):
        if self.size[stacknum] == 0:
            return True
        else:
            return False
    
    def indexoftop(self,stacknum):
        offset=stacknum * self.stackSize
        return offset + self.size[stacknum]-1

    def push(self,item,stacknum):
        if self.isFull(stacknum):
            return 'Full'
        else:
            self.size[stacknum] +=1
            self.cutlist[self.indexoftop(stacknum)] = item
    
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return 'empty'
        else:
            value=self.cutlist[self.indexoftop(stacknum)]
            self.cutlist[self.indexoftop(stacknum)] = 0
            self.size[stacknum] -=1
            return value
        
    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            return 'empty'
        else:
            value=self.cutlist[self.indexoftop(stacknum)]
            return value
custom=MultiStack(6)
print(custom.isFull(0))
print(custom.isEmpty(1))
custom.push(1,0)
custom.push(2,0)
custom.push(3,2)
print(custom.peek(0))
