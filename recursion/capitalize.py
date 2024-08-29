def capitalizeFirst(arr):
    result=[]
    if len(arr) ==0:
        return arr
    result.append(arr[0].upper())
    return result+ capitalizeFirst(arr[1:])
print(capitalizeFirst(['car', 'taco', 'banana']))
