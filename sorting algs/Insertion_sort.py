array=[1,3,2,5,4,6,7,10,9,8]
def InsertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return (array)
InsertionSort(array)
print(array)
