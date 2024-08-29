def findmincost(array,row,col,maxcost):
    if maxcost<0:
        return 0
    elif row ==0 and col ==0:
        if array[0][0] - maxcost == 0:
            return 1
        else:
            return 0
    elif row==0:
        return findmincost(array,0,col-1,maxcost-array[row][col])
    elif col==0:
        return findmincost(array,row-1,0,maxcost-array[row][col])
    else:
        op1=findmincost(array,row-1,col,maxcost-array[row][col])
        op2=findmincost(array,row,col-1,maxcost-array[row][col])
        return op1+op2
array = [[4,7,1,6],
        [5,7,3,9],
        [3,2,1,2],
        [7,1,6,3]]
print(findmincost(array,3,3,25))