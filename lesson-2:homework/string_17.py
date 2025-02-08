a = input()
con1 = ["A","a","E","e","I","i","O","o","U","u"]
result = ""
for char in a :
    if char in con1 :
        result = result + "*"
    else :
        result = result + char

print(result)