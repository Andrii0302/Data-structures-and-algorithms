import numpy as np
import array

# my_array=array.array("i")
# print(my_array)
my_array=array.array("i", [1,2,3,4])
# print(my_array)
#my_array.insert(len(my_array),5)
#print(my_array)
def traverse(my_array):
    for i in my_array:
        print(i)

        
# traverse(my_array)
def accessele(my_array,index):
    if index >= len(my_array):
        print("no element on this index")
    else:
        print(my_array[index])
index=2
#accessele(my_array,index)

def linear_search(my_array,target):
    for i in range(len(my_array)):
        if my_array[i]==target:
            return f'index of the element is {i}'
    return f'the {target} element is abcent in this array'
# print(linear_search(my_array,7))
def delete_from_array(my_array):
    my_array.remove(3)
    print(my_array)
delete_from_array(my_array)
# np_array= np.array([],dtype=int)
# print(np_array)
# np_array= np.array([1,2,3,4])
# print(np_array)