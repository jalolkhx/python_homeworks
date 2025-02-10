my_dict = {'name': 'Alice', 'age': 25}

value = my_dict.get('name')
print(value)  

value = my_dict.get('height', 'Key not found')
print(value)
