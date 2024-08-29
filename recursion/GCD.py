# GREATEST COMMON DIVISOR - Euclidean algorithm
def GCD(a,b):
    assert int(a) == a and int(b) == b , 'not integers'
    if a <0:
        a*=-1
    if b < 0:
        b*=-1
    if b==0:
        return a
    else:
        return GCD(b,a%b)
print(GCD(48,-18))