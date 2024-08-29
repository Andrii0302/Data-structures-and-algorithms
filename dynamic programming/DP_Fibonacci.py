# Top Down memoization
def FibMemo(n,memo={}):
    if n==1:
        return 0
    if n ==2:
        return 1
    if not n in memo:
        memo[n]= FibMemo(n-1,memo)+FibMemo(n-2,memo)
    return memo[n]
print(FibMemo(6))


# Bottom Up Tabulation
def FibTab(n):
    tb=[0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]
print(FibTab(6))