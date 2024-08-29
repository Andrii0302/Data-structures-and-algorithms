def nestedEvenSum(object,sum=0):
    for i in object:
        if type(object[i]) is dict:
            sum+=nestedEvenSum(object[i])
        elif type(object[i]) is int and object[i]%2==0:
            sum+=object[i]
    return sum





