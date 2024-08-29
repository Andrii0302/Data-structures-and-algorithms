def house_robber(hlist,current):
    if current >= len(hlist):
        return 0
    else:
        return max(hlist[current] + house_robber(hlist, current + 2), house_robber(hlist, current + 1))
hlist=[6,7,1,30,8,2,4]
print(house_robber(hlist,0))

