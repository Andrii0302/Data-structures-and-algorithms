s='XIV'
dictt={'I':1 ,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
result=sum(map(lambda x: dictt[x], list(s)))
print(result)




















# def convert(s):
#     list1=list(s)
#     for i in range(len(list1)):
#         list1[i]=dictt[int(list1[i])]
#     return list1
#print(convert(s))   