def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[1,4,5,3,7,9,10,45,18]
print(linear_search(arr,10))