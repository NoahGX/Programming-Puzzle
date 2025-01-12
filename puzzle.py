def pyramid_path(pyramid, target, row=0, idx=0, product=1, path=""):
    # Multiply product by the current cell value
    product *= pyramid[row][idx]

    # If the last row is reached, check if target is met
    if row == len(pyramid) - 1:
        return path  # valid path found
    else:
        return None  # no path found
    
    # Otherwise, try going left
    left = pyramid_path(pyramid, target, row+1, idx, product, path+"L")

    # If path is found while going left, return it
    if left is not None:
        return left

    # If left does not succeed, try going right
    right = pyramid_path(pyramid, target, row+1, idx+1, product, path+"R")

    # If path is found while going right, return it
    return right

# Main function
if __name__ == "__main__":
    # Set the target
    target = 720
    
    # Set the pyramid
    pyramid = [
        [2],
        [4, 3],
        [3, 2, 6],
        [2, 9, 5, 2],
        [10, 5, 2, 15, 5]
    ]

    path = pyramid_path(pyramid, target)
    print("Path: ", path)
