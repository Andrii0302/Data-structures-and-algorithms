import numpy as np

twodimarr= np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
#print(twodimarr)
#newarr=np.insert(twodimarr,4,[[1,2,3,4]], axis=0)
#print(newarr)
newarr=np.append(twodimarr,[[1,2,3,4]], axis=0)
#print(newarr)
def access(newarr,row,col):
    if row >= len(newarr) or col >= len(newarr[0]):
        print("Incroect")
    else:
        print(newarr[row][col])
# access(newarr, 2,3)
def trav(newarr):
    for i in range(len(newarr)):
        for j in range(len(newarr[0])):
            print(newarr[i][j])
#trav(newarr)

def findi(newarr,target):
    for i in range(len(newarr)):
        for j in range(len(newarr[0])):
            if newarr[i][j] == target:
                print(i, j)
    return -1
#findi(newarr,target=11)
newarr1=np.append(twodimarr,[[1,2,3,4]], axis=0)
def deltwo(newarr1):
    newarr1=np.delete(newarr1, 0, axis=1)
    print(newarr1)
#deltwo(newarr1)
