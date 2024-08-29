def palindromic_subsequence(str1,start,end):
    if start>end:
        return 0
    elif start==end:
        return 1
    elif str1[start]==str1[end]:
        return 2+palindromic_subsequence(str1,start+1,end-1)
    else:
        op1=palindromic_subsequence(str1,start,end-1)
        op2=palindromic_subsequence(str1,start+1,end)
        return max(op1,op2)
str1='ELRMENMET'
print(palindromic_subsequence(str1,0,len(str1)-1))