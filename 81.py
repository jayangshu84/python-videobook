while True:
    usr = raw_input("Enter Username: ")
    with open("users.txt", "r")as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]
    if usr in users:
        print("Username exists!")
        continue
    else:
        print("Username is fine!")
        break

while True:
    notes = []
    psw = raw_input("Enter your Password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need atleast one number.")
    if not any(i.isupper() for i in psw):
        notes.append("You need atleast one uppercase letter.")
    if len(psw) < 5:
        notes.append("You need atleast 5 character.")
    if len(notes) == 0:
        print("Password is fine.")
        break
    else:
        print("Please check the following:")
        for note in notes:
            print(note)