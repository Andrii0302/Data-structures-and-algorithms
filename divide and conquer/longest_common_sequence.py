def sub_sequnce(str1,str2,index1,index2):
    if index1==len(str1) or index2==len(str2):
        return 0
    if str1[index1]==str2[index2]:
        return 1+sub_sequnce(str1,str2,index1+1,index2+1)
    else:
        op1=sub_sequnce(str1,str2,index1,index2+1)
        op2=sub_sequnce(str1,str2,index1+1,index2)
        return max(op1,op2)

str1='elephant'
str2='eretpat'
print(sub_sequnce(str1,str2,0,0))
