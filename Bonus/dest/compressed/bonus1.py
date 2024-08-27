#bonus 1
"""user_password : str = input("Enter a password: ")

while True:
    guess = input('Input your password: ')
    if guess == user_password:
        print("Matches!")
        exit()
    else:
        print("It don't match") """

# user_password = input("Enter password: ")

# while user_password != "pass123":
#    user_password = input("Enter password: ")

# print("Password was correct")

# bonus 2
"""x = 1

while x <= 6:
    print(x)
    x = x + 1 """

"""countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)"""

# bonus 3

"""" = ['pasta', 'pizza', 'salad']
for meal in meals:
    print(meal.capitalize())

for char in 'meals':
    print(char.capitalize())

for item in ['hello', 'hi']:
    print(item.upper())

colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)"""

# bonus 4

"""filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)"""

# bonus 4.5

"""ranking = ['John', 'Sen', 'Lisa']

name = input("Enter a name: ").capitalize()
print(ranking.index(name) + 1)"""

# bonus 4.6

"""mood = 'mood'
strength = float(100)
rank: int = 100"""

#bonus coding exercise 2 day 5
#ips = ['100.122.133.105', '100.122.133.111']
#user_choice = int(input("Enter an input, 0 or 1"))
#chosen_ip = ips[user_choice]
#print("You chose " + chosen_ip)

"""contents = ["All your base are belong to us",
            "The quick brown fox jumped over the lazy dog",
            "Anta boke?"]

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"Files/{filename}", 'w')
    file.write(content)"""

"""new_memb = input("Enter a new member: ")

file = open("Files/members.txt", 'r')
new_members = file.readlines()
file.close()

new_members.append(new_memb + "\n")

file = open("Files/members.txt", 'w')
file.writelines(new_members)
file.close()"""

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
contents = "Hello" + "\n"

for filename in filenames:
    file = open(f"Files/{filename}", 'w')
    file.write(contents)
