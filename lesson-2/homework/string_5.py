a = input()
b = a.replace("A","").replace("E","").replace("U","").replace("I","").replace("O","")
c = b.replace("a","").replace("e","").replace("u","").replace("i","").replace("o","")
vowels_num = len(a)-len(c)
d = c.replace(" ","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","")
consonants = len(d)
print(f"Vowels: {vowels_num}")
print(f"consonants: {consonants}")
# code works for the inputs that only contain numbers and letters