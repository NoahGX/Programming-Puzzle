def triangle_path(pyramid, row, idx, target, product, path):
    product *= pyramid[row][idx]
    if row == len(triangle - 1):
        if product == target:
            return path
    else:
        return None

# Traingle pyramid
triangle = [
    [2],
    [4, 3],
    [3, 2, 6],
    [2, 9, 5, 2],
    [10, 5, 2, 15, 5]
]

result *= triangle[row][idx]
Left = triangle[row + 1][idx]  # left is next row, same index
Right = triangle[row + 1][idx + 1]  # right is next row, next index

product = 0
path = ""
target = -1

for row in triangle:
    for idx in row:
        print(result, path=' ')
    print()
