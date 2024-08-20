def avg():
    column = []
    for line in open('../Files/numbers.txt', 'r').readlines():
        column.append(line.strip())

    sum_number = 0
    for index, number in enumerate(column):
        sum_number += int(number)

    return sum_number / len(column)

print(avg())

