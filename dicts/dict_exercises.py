# Count word frequency
def count_word_freq(lst1):
    result={}
    for i in lst1:
        result[i] = result.get(i, 0) + 1
    return result
#print(count_word_freq(['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] ))


# Merge two dict2 and sumup their values if the key is identical
def merge_dicts(dict1, dict2):
    result = dict1
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
#print(merge_dicts({'a': 1, 'b': 2, 'c': 3},{'b': 3, 'c': 4, 'd': 5}))


# Key with highest value
def max_value_key(my_dict1):
    max1=float('-inf')
    for i in my_dict1:
        if max1 < my_dict1[i]:
            max1=my_dict1[i]
            letter=i
    return letter
# print(max_value_key({'a': 5, 'b': 9, 'c': 2}))
# or like this
    print(max(my_dict,key=my_dict.get))


# Reverse the key and a value {1:'a'} --- {'a':1}
def reverse_dict(my_dict):
    result={}
    for key,value in my_dict.items():
        result[value]=key
    return result
#print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))
# or with compreh
def reverse_dict2(my_dict):
    return {value:key for key, value in my_dict.items()}
#print(reverse_dict2({'a': 1, 'b': 2, 'c': 3}))
        

# Conditional filter
def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}


# Same frequency
def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
        
    return count_elements(list1) == count_elements(list2)
    
        
