filepath = "../Files/Journal.txt"

with open(filepath, 'r') as file:
    entry = input("Enter today's date: ")
    entries = file.readlines()
    entries.append(entry + '\n')
    rate = input("How do you rate your mood today from 1 to 10? ")
    entries.append(rate + '\n')
    thoughts = input("Let your thoughts flow: ")
    entries.append(thoughts + '\n' + 'End of Entry' + '\n' + '\n')

with open(filepath, 'w') as file:
    file.writelines(entries)