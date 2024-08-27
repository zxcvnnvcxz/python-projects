files_path = "../Files/"
filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"{files_path}{filename}")
    a = file.read()
    print(a)