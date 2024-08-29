# Top down memoization
def number_factor(n,memo={}):
    if n in [0,1,2]:
        return 1
    elif n==3:
        return 2
    else:
        if n not in memo:
            memo[n]=number_factor(n-1,memo)+number_factor(n-3,memo)+number_factor(n-4,memo)
        return memo[n]
print(number_factor(5))

        # sub1=number_factor(n-1)
        # sub2=number_factor(n-3)
        # sub3=number_factor(n-4)
        # return sub1+sub2+sub3
# Bottom Up Tabulation

def number_factor_tab(n):
    tb = [1, 1, 1, 2]
    for i in range(4,n+1):
        tb.append(tb[i-1]+tb[i-3]+tb[i-4])
    return tb[n]
print(number_factor_tab(5))
            