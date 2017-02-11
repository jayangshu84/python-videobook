def count_words(filepath):
    with open(filepath, 'r') as file: # investigate what this is doing
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

print (count_words("words1.txt"))
