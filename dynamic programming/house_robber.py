# Top Down Memo
def house_robberMemo(hlist,current,memo={}):
    if current >= len(hlist):
        return 0
    else:
        if current not in memo:
            memo[current]=max(hlist[current] + house_robberMemo(hlist, current + 2,memo), house_robberMemo(hlist, current + 1,memo))
        return memo[current]

# Bottom Up Tabulation
def house_robber_tab(hlist):
    tb=[0]*(len(hlist)+2)
    for i in range(len(hlist)-1,-1,-1):
        tb[i]=max(hlist[i]+tb[i+2],tb[i+1])
    return tb[0]
        

hlist=[6,7,1,30,8,2,4]
print(house_robberMemo(hlist,0))
print(house_robber_tab(hlist))