txt = input("enter the string: ")
list_txt = list(txt)
list1 = []
list_vowels = ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'O', 'I', 'U']
length = len(txt)
i = 2

while i<length-1 :
    if txt[i] in list_vowels :
        i = i+1
    elif txt[i] in list1 :
        i = i+1
    else :
        list1.append(txt[i])
        list_txt[i] = txt[i] + "_"
        i=i+3

the_result = ''.join(list_txt)
print(the_result)