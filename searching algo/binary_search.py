def binary_search(arr, target):
    left=0
    right=len(arr)-1
    mid = (left + right) // 2
    while not (arr[mid]==target) and left <= right:
        if target < arr[mid]:
            right=mid-1
        else:
            left=mid+1
        mid=(left+right)//2
    if arr[mid]==target:
        return mid
    else:
        return -1
    


arr=[1,2,3,4,5,6,7,8,9]
target=8
print(binary_search(arr,target))
