d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word doesn't exists"

word = raw_input("Enter Word: ").lower()
print(vocabulary(word))