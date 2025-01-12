def triangle_path(pyramid, row, idx, target, product, path):
    # Multiply running product by the current cell value
    product *= pyramid[row][idx]

    # If the last row is reached, check if target is met
    if row == len(triangle - 1):
        return path  # valid path found
    else:
        return None  # no path found
    
    # Go left
    left = triangle_path(triangle, target, row+1, idx, product, path+"L")

    # If path is found while going left, return it
    if left is not 0:
        return left

    # Go right
    right = triangle_path(triangle, target, row+1, idx+1, product, path+"R")

    # If path is found while going right, return it
    return right

# Main function
if __name__ = "__main__":
    # Set the target
    target = 720
    
    # Triangle pyramid
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
