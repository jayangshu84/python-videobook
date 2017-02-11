# Solution 1 using replace
def count_words(filepath):
    with open(filepath, "r") as file:
        strng = file.read()
        strng = strng.replace(",", " ")
        strng_list = strng.split(" ")
        return len(strng_list)

print (count_words("words2.txt"))

# Solution 2 using library
import re


def count_words_re(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string_list = re.split(",| ", string)
        return len(string_list)


print(count_words_re("words2.txt"))