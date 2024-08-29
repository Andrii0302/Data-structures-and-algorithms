def convert_string(str1,str2,index1,index2,memo={}):
    if index1==len(str1):
        return len(str2)-index2
    if index2==len(str2):
        return len(str1)-index1
    if str1[index1]==str2[index2]:
        return convert_string(str1,str2,index1+1,index2+1)
    else:
        if (index1,index2) not in memo:
            delete=1+convert_string(str1,str2,index1,index2+1)
            insert=1+convert_string(str1,str2,index1+1,index2)
            replace=1+convert_string(str1,str2,index1+1,index2+1)
            memo[(index1,index2)]=min(delete,insert,replace)
        return memo[(index1,index2)]
    
def convert_string_bottom_up(str1, str2,tempDict):
    m, n = len(str1), len(str2)
    tempDict = [[0] * (n + 1) for _ in range(m + 1)]
    
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                tempDict[i][j] = j
            elif j == 0:
                tempDict[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                tempDict[i][j] = tempDict[i - 1][j - 1]
            else:
                tempDict[i][j] = 1 + min(tempDict[i][j - 1],   
                                tempDict[i - 1][j],   
                                tempDict[i - 1][j - 1]) 
    return tempDict[m][n]


str1 = "kitten"
str2 = "sitting"
print(convert_string_bottom_up(str1, str2,{}))

str1='sunday'
str2='saturday'
print(convert_string(str1,str2,0,0))