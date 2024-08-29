def convert_string(str1,str2,index1,index2):
    if index1==len(str1):
        return len(str2)-index2
    if index2==len(str2):
        return len(str1)-index1
    if str1[index1]==str2[index2]:
        return convert_string(str1,str2,index1+1,index2+1)
    else:
        delete=1+convert_string(str1,str2,index1,index2+1)
        insert=1+convert_string(str1,str2,index1+1,index2)
        replace=1+convert_string(str1,str2,index1+1,index2+1)
        return min(delete,insert,replace)
str1='sunday'
str2='saturday'
print(convert_string(str1,str2,0,0))
