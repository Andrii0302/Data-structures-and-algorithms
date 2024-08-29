import array
#step 1
arr=array.array("i", [1,2,3,4,5])
for i in arr:
    print(i)

#step 2
print()
print(arr[2])
print()

#step 3
arr.append(6)
print(arr)
print()

#step 4
arr.insert(len(arr),7)
print(arr)
print()

#step 5
arr1=array.array('i',[8,9,10])
arr.extend(arr1)
print(arr)
print()

#step 6
templist= [11,12,13]
arr.fromlist(templist)
print(arr)
print()

#step 7
arr.remove(13)
print(arr)
print()

#step 8
arr.pop()
print(arr)
print()

#step 9
print(arr.index(11))
print()

#step 10
arr.reverse()
print(arr)
print()

#step 11
print(arr.buffer_info())
print()

#step 12
print(arr.count(5))
print()

#step 13
strTmp = arr.tobytes()
print(strTmp)
print()

#step 14
print(arr.tolist())
print()

#step 15
print(arr[1:6])
print()


