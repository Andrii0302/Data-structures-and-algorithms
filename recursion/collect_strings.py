def collectStrings(obj):
    arr=[]
    for i in obj:
        if type(obj[i]) is dict:
            arr.extend(collectStrings(obj[i]))
        elif type(obj[i]) is str:
            arr.append(obj[i])
    return arr