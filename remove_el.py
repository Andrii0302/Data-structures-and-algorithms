nums = [3,2,2,3]
val=3
k=0
for i in nums[:]:
    if i==val:
        nums.remove(i)
    else:
        k+=1
print(k)
print(nums)