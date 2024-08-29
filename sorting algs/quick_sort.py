array=[3,1,2,5,4,6,7,10,9,8]
def swap(array,index1,index2):
    array[index1],array[index2] = array[index2],array[index1]
def pivot(array,pivot_index,end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1,end_index+1):
        if array[i] < array[pivot_index]:
            swap_index += 1
            swap(array,swap_index,i)
    swap(array,pivot_index,swap_index)
    return swap_index
    
def quickSort_h(array,left,right):
    if left<right:
        pivot_index = pivot(array,left,right)
        quickSort_h(array,left,pivot_index-1)
        quickSort_h(array,pivot_index+1,right)
    return array
def quickSort(array):
    return quickSort_h(array,0,len(array)-1)
quickSort(array)
print(array)

