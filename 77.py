from datetime import datetime

age = int(raw_input("What is your age?: "))
year_birth = datetime.now().year -age

print("You are born back in %s" %year_birth)