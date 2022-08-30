# HASHTAG GENERATOR
def generate_hashtag(s):
    t = ""
    new_s = ""
# Check if the length of the String is more than 140 characters and return False
    if len(s) > 140:
        return False
# Check if it is a blank input and return False
    elif s == "":
        return False
# Convert the String to a List
    str_to_list = list(s.split(" "))
# Check each word in the List
    for ele in str_to_list:
# Capitalize the first letter
        ele = ele.capitalize()
# Add the capitalized word to a new List
        t += ele
        str_to_list = list(t.split(" "))
# Add a hashtag to the beginning of the List
        str_to_list.insert(0, "#")
# Convert back to a String
    for ele in str_to_list:
        new_s += ele
# Return the String to the main function
    return new_s


phrase = input("Enter the phrase you want to Hashtag:")
print(generate_hashtag(phrase))
