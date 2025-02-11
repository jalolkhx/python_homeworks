list1 = []
elements1 = input("Enter the element for list 1: ")
while elements1 != "" :
    list1.append(elements1)
    elements1 = input("Enter the element for list 1 or click Enter to finish: ")

list2 = []
elements2 = input("Enter the element for list 2: ")
while elements2 != "" :
    list2.append(elements2)
    elements2 = input("Enter the element for list 2 or click Enter to finish: ")

adding_list = list1 + list2 
final_list = []

for i in adding_list:
    if i in list1 and i in list2:
        pass
    else :
        final_list.append(i)

print(f"your list 1 is {list1}")
print(f"your list 2 is {list2}")

print(f"the uncommon elements: {final_list}")
