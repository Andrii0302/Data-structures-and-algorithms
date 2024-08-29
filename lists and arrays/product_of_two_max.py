
def max_product(arr):
    max1=arr[0]
    for i in arr:
        if max1<i:
            max1=i
    first=max1
    arr.remove(max1)
    return (max(arr)*first)            
        
#print(max_product([1,7,3,4,9,5]))

def middle(lst):
    lst=lst[1:len(lst)-1]
    return (lst)
#print(middle([1,2,3,4]))

def diagonal_sum(matrix):
    sum=0
    for i in range(len(matrix)):
        sum+=matrix[i][i]
    return sum
#print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))
def first_second(my_list):
    max1=my_list[0]
    for i in range(len(my_list)):
        if max1 < my_list[i]:
            max1=my_list[i]
    first=max1
    my_list.remove(max1)
    return [first, max(my_list)]
#print(first_second([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))

def remove_duplicates(arr):
    s=[]
    for i in range(len(arr)):
        if arr[i] not in s:
            s.append(arr[i])
        else:
            continue
            
    return s
#print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

def pair_sum(lst, sum):
    s=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i] !=lst[j]:
                if lst[i]+lst[j]==sum:
                    s.append(f'{lst[i]}+{lst[j]}')
    return s
#print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

def contains_duplicate(nums):
    leng=len(nums)
    if leng==len(set(nums)):
        return True
    else:
        return False
#print(contains_duplicate([1,2,3,1]))

def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    if list1.sort() == list2.sort():
        return True
    else:
        return False
#print(permutation([1,2,3],[2,3,1]))

def rotate(matrix):
    matrix=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix
#print(rotate([[1,2,3],[4,5,6],[7,8,9]]))