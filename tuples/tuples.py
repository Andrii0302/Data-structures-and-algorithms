# Inititalization
t='a','b','c','d'
t=('a','b','c','d')

t=('a',) #tuple with one element

t=tuple('abcd') # tuple with function, each character will be separate tuple element

# How to access elements of tuple
el=t[0]

# Traverse
# for i in range(len(t)):
#     print(t[i])

# Element search
def search(t,target):
    for i in t:
        if i == target:
            print(i)
#search(t,target='c')

def search1_bool(t,target):
    print(target in t)
#search1_bool(t,target='c')

def search2(t,target):
    print(t.index(target))
#search2(t,target='c')


# Tuple operations/ functions

newt1=(1,2,3,4,5)
newt2=(6,7,8,9,10)
#print(newt1+newt2)
#print(newt1 *4) #repetition
#print(2 in newt1)

#print(newt1.count(2))

#print(newt1.index(4))

#print(len(newt1))

#print(tuple([1,2,3,4])) # convertion

def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple
#print(insert_value_at_beginning((2,3,4),1))

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)
#print(concatenate_strings(('Hello', 'World', 'from', 'Python')))

def get_diagonal(tup):
    a=[]
    for i in range(len(tup)):
        a.append(tup[i][i])
    return tuple(a)

#print(get_diagonal(((1, 2, 3),(4, 5, 6),(7, 8, 9))))

def common_elements(tuple1,tuple2):
    a=[]
    for i in tuple1:
        if i in tuple2:
            a.append(i)
    return tuple(a)
print(common_elements((1, 2, 3, 4, 5),(4, 5, 6, 7, 8)))
        
