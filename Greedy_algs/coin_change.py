money=[1,2,5,10,20,50,100,1000]
target=213

def coin_change(money,target):
    result=[]
    index=len(money)-1
    while True:
        if target - money[index]<0:
            index-=1
        else:
            result.append(money[index])
            target=target -money[index]
        if target==0:
            break
    return result
print(*coin_change(money,target))    