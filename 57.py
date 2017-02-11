import json
from pprint import pprint

with open("exdict.json", "r") as file:
    d = json.loads(file.read())

pprint(d)
