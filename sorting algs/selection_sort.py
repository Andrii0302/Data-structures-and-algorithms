array=[1,3,2,5,4,6,7,10,9,8]
def selectionSort(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1, len(array)):
            if array[min_index]>array[j]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]
    return array
selectionSort(array)
print(array)