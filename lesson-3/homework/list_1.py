list1 = []
n = input("enter element (or press ENTER to stop): ")
while n != "" :
    list1.append(n)
    n = input("Enter next element (or press ENTER to stop): ")

element1 = input("Enter the element to count: ")

if element1 in list1 :
    print(f"{element1} is attended in the list {list1.count(element1)} times")
else :
    print(f"{element1} is not in the list")