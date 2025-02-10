my_set = {1,2,3,4,5,6,7,8,9}
element = 0
if element not in my_set:
    my_set.add(element)
    print(f"Element {element} added to the set.")
else:
    print(f"Element {element} is already in the set.")

print("Updated set:", my_set)