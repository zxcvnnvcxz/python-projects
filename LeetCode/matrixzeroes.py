def MatrixZeroes(matrix): # My Solution
    length = len(matrix) - 1
    zero_map = []
    for index, row in enumerate(matrix):
        flag = None
        for idx, number in enumerate(row):
            if number == 0:
                flag = True
                zero_map.append([index, idx])
        if flag:
            for i in range(len(row)):
                row[i] = 0
    while zero_map:
        y = 0
        x = zero_map[0][1]
        while y <= length:
            matrix[y][x] = 0
            y += 1
        zero_map.pop(0)
    return matrix


# Optimal Solution
def setMatrixZeroes(matrix):
    rows = len(matrix) # How many rows do we have
    cols = len(matrix[0]) # How many columns do we have
    first_row_zero = False # Define a flag for later
    first_col_zero = False # ''

    # Determine if the first row and first column should be zeroed
    for i in range(rows): # for every number in each row
        for j in range(cols): # for every number in each column
            if matrix[i][j] == 0:
                if i == 0:
                    first_row_zero = True # Mark the rest of row for zero
                if j == 0:
                    first_col_zero = True # Mark the rest of col for zero
                matrix[i][0] = 0 # Change the first column [i-th] to a zero
                matrix[0][j] = 0 # Change the first row [j-th] to a zero

    # Zero out the rest of the cells based on markers in the first row and column
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Zero out the first row if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Zero out the first column if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1,1,1],
              [1,0,1],
              [1,1,1]]
    print(setMatrixZeroes(matrix))