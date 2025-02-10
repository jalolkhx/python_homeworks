my_dict = {'name': 'Alice', 'age': 25}

key = 'name'
if key in my_dict:
    pair = (key, my_dict[key])
    print(pair)  
else:
    print('Key not found')
