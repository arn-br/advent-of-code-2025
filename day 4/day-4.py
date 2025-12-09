def read_into_array():
    matrix = []

    with open("input.txt", "r") as f:
        for line in f:
            matrix.append(list(line.strip()))
    
    return matrix

def calculate_count(matrix, i, j):
    #i is row num
    #j is column num
    count = 0
    i_len = len(matrix)
    j_len = len(matrix[i])

    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    for ki, kj in neighbors:
        new_i = i + ki
        new_j = j + kj
    
        if 0 <= new_i < i_len and 0 <= new_j < j_len:
            if matrix[new_i][new_j] == "@":
                count += 1
    
    if count < 4:
        return True
    
    return False

def part1(matrix):
    res = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@":
                val = calculate_count(matrix, i, j)

                if val == True:
                    res += 1
    
    print(res)
    return res

def part2(matrix):

    res2 = 0
    go = True

    indexes = []

    while go:
        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                if matrix[i][j] == "@":
                    val = calculate_count(matrix, i, j)

                    if val == True:
                        indexes.append([i, j])
                        res += 1
                
                elif matrix[i][j] == "x":
                    matrix[i][j] = "."

        for elem in indexes:
            matrix[elem[0]][elem[1]] = "x"

        indexes.clear()        

        if res == 0:
            go = False
        else:
            res2 += res

    print(res2)
    return res

def main():
    print("Part 1:")
    part1(read_into_array())

    print("Part 2:")
    part2(read_into_array())

if __name__ == "__main__":
    main()