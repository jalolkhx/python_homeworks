words = input()
con_1 = words.split(" ")
l = len(con_1)
result = ""
for i in range(0,l):
    result = result + "_" + con_1[i]

print(result[1:])