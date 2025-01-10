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

for row in triangle:
    for num in row:
        print(num, end=' ')
    print()
