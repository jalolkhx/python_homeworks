my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
result = dict(zip(my_dict.values(), my_dict.keys()))
print(result)