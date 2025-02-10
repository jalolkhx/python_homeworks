dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}

common_keys = set(dict1.keys()) & set(dict2.keys())
print(common_keys) 