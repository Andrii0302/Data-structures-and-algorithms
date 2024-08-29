def findmincost(array,row,col):
    if row ==-1 or col ==-1:
        return float('inf')
    if row ==0 and col ==0:
        return array[0][0]
    else:
        op1=findmincost(array,row-1,col)
        op2=findmincost(array,row,col-1)
        return +array[row][col]+min(op1,op2)
array = [[4,7,8,6,4],
        [6,7,3,9,2],
        [3,8,1,2,4],
        [7,1,7,3,7],
        [2,9,8,9,3]]
print(findmincost(array,4,4))