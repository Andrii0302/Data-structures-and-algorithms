def productOfArray(arr):
    if arr ==[]:
        return 1
    else:
        return arr.pop() * productOfArray(arr)
print(productOfArray([1,2,3,10]))

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])



