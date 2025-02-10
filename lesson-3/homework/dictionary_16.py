my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 3: 'd'}
set1 = set(my_dict.keys())
set2 = set(my_dict.values())
result = set1 & set2
if result == set() :
    print("there is no common values with keys")
else :
    print("common values with keys: ", result)