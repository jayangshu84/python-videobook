import json

with open("company1.json", "r+") as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName = "J", lastName = "S"))
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()