import glob

myfiles = glob.glob("Files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
