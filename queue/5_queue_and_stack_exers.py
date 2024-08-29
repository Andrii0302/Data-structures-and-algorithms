class Queue():
    def __init__(self):
        self.cats=[]
        self.dogs=[]
    
    def enqueue(self,animal,type):
        if type =='Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat=self.cats.pop(0)
            return cat
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog=self.dogs.pop(0)
            return dog
    def dequeueAny(self):
        if len(self.cats) ==0:
            result=self.dogs.pop(0)
        else:
            result=self.cats.pop(0)
        return result
custom=Queue()
custom.enqueue('Cat1','Cat')
custom.enqueue('Cat2','Cat')
custom.enqueue('Dog1','Dog')
custom.enqueue('Cat3','Cat')
custom.enqueue('Dog2','Dog')
print(custom.dequeueCat())
print(custom.dequeueCat())
print(custom.dequeueAny())
print(custom.dequeueAny())

    