from itertools import permutations
n=3
k=3
list1=[i+1 for i in range(n)]
store=[]
for i in permutations(list1):
    store.append(i)
result=''
s=list(map(str,store[k]))
for i in range(n):
    result+=s[i]
print(result)