# stack using list without size limit
class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,value):
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
stack1=Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)
#stack1.pop()
print(stack1.peek())
print()
# print(stack1.isEmpty())
print(stack1)