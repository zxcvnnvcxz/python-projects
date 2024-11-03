from heapq import heappush


def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    initialColor = image[sr][sc]
    temp = image
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]

    dfs(sr, sc, temp, image, color, delRow, delCol, initialColor)

    return temp

def dfs(row, col, temp, image, color, delRow, delCol, initialColor):
    temp[row][col] = color
    n = len(image)
    m = len(image[0])

    for i in range(4):
        nrow = row + delRow[i]
        ncol = col + delCol[i]
        if 0 <= nrow < n and 0 <= ncol < m and image[nrow][ncol] == initialColor and temp[nrow][ncol] != color:
            dfs(nrow, ncol, temp, image, color, delRow, delCol, initialColor)


def flood_fill1(image, sr, sc, new_color):
    if image[sr][sc] == new_color:
        return image

    original_color = image[sr][sc]
    rows, cols = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
            return
        image[r][c] = new_color
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    dfs(sr, sc)
    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))