# Top Down Memo
class Item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight

def zoknapsack_memo(items,capacity,current,memo={}):
    if capacity<=0 or current<0 or current>=len(items):
        return 0
    elif (capacity,current) in memo:
        return memo[(capacity,current)]
    elif items[current].weight<=capacity:
        if (capacity,current) not in memo:
            memo[(capacity,current)]=max(items[current].profit+zoknapsack_memo(items,capacity-items[current].weight,current+1,memo), zoknapsack_memo(items,capacity,current+1,memo))
        return memo[(capacity,current)]
    else:
        return 0
    
def zoknapsack_tab(items,capacity,current):
    if capacity<=0 or current<0 or current>=len(items):
        return 0
    numofrows=len(items)+1
    dp = [[0 for i in range(capacity+2)] for j in range(numofrows)]
    for row in range(numofrows-2,-1,-1):
        for col in range(1,capacity+1):
            profit1=0
            profit2=0
            if items[row].weight<=col:
                profit1=items[row].profit+dp[row+1][col-items[row].weight]
            profit2=dp[row+1][col]
            dp[row][col]=max(profit1,profit2)
    return dp[0][capacity]
mango=Item(31,3)
apple=Item(26,1)
orange=Item(17,2)
banana=Item(72,5)
items=[mango,orange,apple,banana]
print(items)
print(zoknapsack_memo(items,7,0))
print(zoknapsack_tab(items,7,0))
