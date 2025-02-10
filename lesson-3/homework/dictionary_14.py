my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
value = 1
list1 = []
for i in my_dict.keys() :
    if my_dict[i] == value :
        list1.append(i)

print(list1)