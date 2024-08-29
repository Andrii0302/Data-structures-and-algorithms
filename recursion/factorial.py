def factorial(n):
    assert n >=0 and int(n) == n , 'The num must be pos int'
    if n in [0,1]:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(4))