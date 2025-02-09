def pyramid_path(pyramid, target, row=0, idx=0, product=1, path=""):
    # Multiply product by the current cell value
    product *= pyramid[row][idx]

    # If the last row is reached, check if target is met
    if row == len(pyramid) - 1:
        return path if product == target else None
    
    # Otherwise, try going left
    left = pyramid_path(pyramid, target, row+1, idx, product, path+"L")
    if left is not None:
        return left

    # If left does not succeed, try going right
    right = pyramid_path(pyramid, target, row+1, idx+1, product, path+"R")
    return right

def main():
    # Read the file
    with open("../data/inputs/pyramid_input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Parse the target on first line
    target = lines[0]
    target = int(target.split(":")[1].strip())

    # Parse pyramid rows
    pyramid = []
    for line in lines[1:]:
        # Split by comma, convert each element to int
        # If there's only one element (e.g. '2'), it becomes [2]
        row_values = [int(x) for x in line.split(",")]
        pyramid.append(row_values)

    # Solve the puzzle
    solution = pyramid_path(pyramid, target)

    # Write the solution to the output file
    output_path = "../data/outputs/pyramid_solution.txt"
    with open(output_path, "w") as output:
        if solution is not None:
            output.write(f"Path: {solution}\n")
        else:
            output.write(f"No valid path round for target = {target}\n")
    print(f"Solution written to {output}")

if __name__ == "__main__":
    main()
