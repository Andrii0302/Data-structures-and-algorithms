def stringifyNumbers(obj):
    new=obj
    for i in obj:
        if type(new[i]) is dict:
            new[i]=stringifyNumbers(new[i])
        elif type(new[i]) is int:
            new[i]=str(obj[i])
    return new
