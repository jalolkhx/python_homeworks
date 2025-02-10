my_dict = {'f':4, 'a': 1, 'b': 2, 'c': 1, 'd': 3}
list1 = list(my_dict.keys())
list1.sort()
list2 = []

for i in list1 :
    list2.append(my_dict[i])

new_dict = dict(zip(list1, list2))
print(new_dict)