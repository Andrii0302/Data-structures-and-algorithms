lst=[3,6,9,11]
target=9
def findPair():
    s=[]
    for i in range(len(lst)):
        for j in range(i+1):
            if lst[i]+lst[j]==target:
                s.append([lst[i],lst[j]])
    return s
print(findPair())


