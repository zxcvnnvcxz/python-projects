password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase


if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")

# To change into a function
"""def strength(password):
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False
    
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
            
    result["digits"] = digit
    
    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    
    result["upper-case"] = uppercase
    
    if all(result.values()):
        return("Strong password")
    else:
        return("Weak Password")"""