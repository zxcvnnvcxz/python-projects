try:
    height = float(input("Enter the height of rectangle: "))
    width = float(input("Enter the width of rectangle: "))
    if height == width:
        exit("That's a square. ")
    area = height * width

    print("The area of rectangle is " + str(area))
except ValueError:
    print("Please enter in numerical format.")