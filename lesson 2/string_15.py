sentence = input()
con1 = sentence.split(" ")
l = len(con1)
result = ""
for i in range(0,l) :
    result = result + con1[i][:1]

print(result)    