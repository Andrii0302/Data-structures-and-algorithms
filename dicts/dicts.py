#ogoloshennia
my_dict={}
eng_sp = dict(one='uno',two='dos',three='tres')
#print(eng_sp)

eng_sp1 = {'one':'uno','two':'dos','three':'tres'}
#print(eng_sp1)

eng_sp3 = dict([('one','uno'),('two','dos'),('three','tres')])
#print(eng_sp3)

# UPDATE
myDict = {'name':'Andy', 'age':28}
myDict['age']=27
myDict['address']='London'
#print(myDict)

# TRAVERSING
def traverse(myDict):
    for key in myDict:
        print(key, myDict[key])
#traverse(myDict)

# SEARCHING
def search_dict(myDict,Value):
    for key in myDict:
        if myDict[key]==Value:return key,Value
    return 'No value'
#print(search_dict(myDict,27))

#REMOVING

del myDict['address'] #O(1)

myDict.pop('age',None) #O(1)

myDict.popitem() #it returns the deleted last element

myDict.clear() #deletes everything #O(n) and O(1)

#print(myDict)

#METHODS
dict1={'name':'Andy', 'age':28, 'address':'No', 'pipi': "pupu"}
newdict=dict1.copy() # copying a dict

newdict={}.fromkeys([1,2,3], 0) # creates new dict with sequance and a value, None is default
#print(newdict)

print(dict1.get('age',27)) # gets a value by key, will return default value or None

print(dict1.items()) # return a list of tuple pairs

print(dict1.keys()) # returns a list of keys

print(dict1.setdefault('no',10)) # returns a value and creates the key with value if was not found

print(dict1.values()) # returns a list of values

somedic={'a':1, 'b':2, 'c':3}
newdict.update(somedic) # updates a dict with another dict
print(newdict)

# DICTIONARY OPERATIONS
numdict={1:'one',2:'two',3:'three',4:'four',5:'five'}
print(3 in numdict) # 'in' works with keys
print('three' in numdict.values()) #works with values

print(len(numdict)) # returns number of pairs

print(all(numdict)) # returns True if there is no False keys (False,None,0)

print(any(numdict)) # returns True if at least one key is True

print(sorted(numdict)) # sorts the keys of dict and returns the list of sorted keys

#DICT comprehension
import random
lst=['Paris','Kyiv','Pipi']
new_dict = {city:random.randint(20,30) for city in lst}
print(new_dict)

soso= {city: temp for (city,temp) in new_dict.items() if temp > 25}
print(soso)