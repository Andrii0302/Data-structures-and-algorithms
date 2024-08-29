from math import sqrt,ceil
array=[1,3,2,5,4,6,7,10,9,8]
def bucketSort(array):
    numberofbuckets=round(sqrt(len(array)))
    maxVal=max(array)
    arr=[]
    for i in range(numberofbuckets):
        arr.append([])
    for j in array:
        index_b=ceil(j*numberofbuckets/maxVal)
        arr[index_b-1].append(j)
    for i in range(numberofbuckets):
        arr[i] = sorted(arr[i])
    k=0
    for i in range(numberofbuckets):
        for j in range(len(arr[i])):
            array[k]=arr[i][j]
            k+=1
    return array
bucketSort(array)
print(array)
