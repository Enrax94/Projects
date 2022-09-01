def pig_latin(text):

    lst = text.split()
    lst2, lst3, punctuation = [], [], []
    output = ""
    for i in lst:
        lst2.extend(i)
        if i == "!" or i == "?":
            punctuation.append(i)
            continue
        lst2.extend(i[0])
        lst2.remove(i[0])
        lst2.extend("ay")
        lst2.extend(" ")
        lst3.extend(lst2)
        lst2.clear()
    lst3.pop()
    if len(punctuation) > 0:
        lst3.extend(" ")
        lst3.extend(punctuation)
    for ele in lst3:
        output += ele
    return output


print("___PIG_LATIN___")
user_input = input("Enter the word you want to translate to Pig Latin:\n")
print("You've entered:\n", user_input)
print("Translated to Pig Latin is:\n", pig_latin(user_input))
