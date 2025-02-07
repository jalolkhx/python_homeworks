sentence = input()
word = input("replacing word: ")
if word in sentence.split(" ") :
    new_word = input("word for replacing: ")
    new_sentence = sentence.replace(word, new_word)
    print(new_sentence)
else:
    print(f"{word} is not found in the sentence")