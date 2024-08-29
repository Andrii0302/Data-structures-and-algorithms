class Item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight

def zoknapsack(items,capacity,current):
    if capacity<=0 or current<0 or current>=len(items):
        return 0
    elif items[current].weight<=capacity:
        profit1=items[current].profit+zoknapsack(items,capacity-items[current].weight,current+1)
        profit2=zoknapsack(items,capacity,current+1)
        return max(profit1,profit2)
    else:
        return 0
mango=Item(31,3)
apple=Item(26,1)
orange=Item(17,2)
banana=Item(72,5)
items=[mango,orange,apple,banana]
print(zoknapsack(items,7,0))


