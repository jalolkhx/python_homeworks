my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 3}

filtered_dict = {k: v for k, v in my_dict.items() if v > 5}
print(filtered_dict)