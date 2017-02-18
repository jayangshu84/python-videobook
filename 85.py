
with open("countries-raw.txt", "r") as file:
    content = file.readlines()

content = [i.strip("\n") for i in content if "\n" in i]
content = [i.strip("\r") for i in content if "\r" in i]
content = [i for i in content if i !=""]
content = [i for i in content if i !="Top of Page"]
content = [i for i in content if len(i) !=1]

with open("countries-clean.txt", "w") as file:
    for i in content:
        file.write(i+"\n")
