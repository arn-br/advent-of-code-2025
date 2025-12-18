def read_into_array(filename):
    matrix = []

    with open(filename, "r") as f:
        for line in f:
            matrix.append(list(line.strip()))
    
    return matrix

def split_beam(pos_row, pos_column, arr):
    if (pos_column - 1) >= 0 and (pos_column + 1) < len(arr[0]):
        arr[pos_row][pos_column-1] = "|"
        arr[pos_row][pos_column+1] = "|"

    return arr

def part1(arr):
    count = 0

    for r in range(len(arr)):
        for c in range(len(arr[r])):

            #find the start
            if arr[r][c] == "S":
                arr[r+1][c] = "|"
            #if there's a split sign, check if it has incoming beam
            elif arr[r][c] == "^" and arr[r-1][c] == "|":
                arr = split_beam(r, c, arr)
                count += 1
            #if there's incoming beam, continue the beam
            elif arr[r][c] == "." and arr[r-1][c] == "|":
                arr[r][c] = "|"

    print(count)

def main():
    print("Part 1:")
    part1(read_into_array("input.txt"))
    #print(read_into_array("test.txt"))

    #print("Part 2:")
    #part2(read_into_array())

if __name__ == "__main__":
    main()