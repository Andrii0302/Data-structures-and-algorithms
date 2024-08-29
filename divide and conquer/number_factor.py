def number_factor(n):
    if n in [0,1,2]:
        return 1
    elif n==3:
        return 2
    else:
        sub1=number_factor(n-1)
        sub2=number_factor(n-3)
        sub3=number_factor(n-4)
        return sub1+sub2+sub3
print(number_factor(5))
