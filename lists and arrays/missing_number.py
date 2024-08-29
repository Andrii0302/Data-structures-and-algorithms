arr=[1,2,3,4,6]
n=5
def missing_number(arr, n):
    for i in range(1,n+1):
        if i in arr:
            continue
        else:
            print(f'the missing number is {i}')
missing_number(arr,n)