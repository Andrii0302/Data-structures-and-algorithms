class Item:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.ratio=value/weight
def knapsackMethod(items,capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    used=0
    total=0
    for i in items:
        if used+i.weight<=capacity:
            used+=i.weight
            total+=i.value
        else:
            unused = capacity - used
            value = i.ratio * unused
            used+=unused
            total+=value
        if used==capacity:
            break
    return total
item1=Item(20,100)
item2=Item(30,120)
item3=Item(10,60)
clist=[item1,item2,item3]
print(knapsackMethod(clist,50))