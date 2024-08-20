flag = 0
while True:
    password = input("Enter new password: ")

# if character length is greater than 8
    if len(password) >= 8:
        flag = flag + 1
# if character contains at least one number
    if any(char.isdigit() for char in password):
        flag = flag + 1
# if character contains at least one uppercase
    if any(char.isupper() for char in password):
        flag = flag + 1

# if 3 conditions true: print("Strong password")
# if 2 conditions true: print("Medium password")
# if 1 condition true: print("Weak password")
    elif flag == 1:
        print("Weak password")
        exit()
    elif flag == 2:
        print("Medium password")
        exit()
    elif flag == 3:
        print("Strong password")
        exit()
    else:
        exit()