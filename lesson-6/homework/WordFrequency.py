with open('sample.txt', 'r') as f:
    dict1 = {}
    txt_str = f.read()
    cleaned = txt_str.replace('.','').replace(',','').replace(':','').replace('!','')
    list1 = cleaned.lower().split()
    total_words = len(list1)
    for i in list1 :
        dict1[i] = list1.count(i)
    sorted_dict = sorted(dict1, key=dict1.get, reverse=True)[:5]
    print("Total words:", total_words)
    print("Top 5 most common words:")
    for i in sorted_dict :
        print(f"{i} - {dict1[i]} times")
    
with open("word_count_report.txt", "w") as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write("Top 5 Words:\n")
    for i in sorted_dict:
        report.write(f"{i} - {dict1[i]}\n")

print("Word count report saved to 'word_count_report.txt'.")
