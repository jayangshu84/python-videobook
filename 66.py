# Solution 1
"""
d = dict(weather = "clima", earth = "terra", rain = "chuva")

userinput = raw_input("Enter Word:")

print (d[userinput])
"""

# Solution 2

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    return d[word]

word = raw_input("Enter Word: ")
print (vocabulary(word))
