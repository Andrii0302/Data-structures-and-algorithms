class Starcookie:
    milk=0.1
    def __init__(self,color,weight=15):
        self.color=color
        self.weight=weight
    def add_weight(self,cookie):
        cookie.weight+=2
        self.weight +=1

starcook=Starcookie('Red')
roundcook=Starcookie('Pink')
starcook.add_weight(roundcook)
print(starcook.__dict__)
print(roundcook.__dict__)