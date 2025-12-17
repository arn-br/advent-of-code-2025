def read_ranges_into_array(filename):
    """
    Reads the ranges from the text file to a 2D array

    input: filename
    returns: 2d array
    """
    matrix = []

    with open(filename, "r") as f:
        for line in f:
            if "-" in line:
                start, end = line.split("-")
                start = int(start.strip())
                end = int(end.strip())
                
                matrix.append(list([start, end]))

    return matrix

def read_ids_into_array(filename):
    """
    Reads the ids from the text file to an array

    input: filename
    returns: array
    """
    matrix = []

    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue
            elif "-" not in line:
                num = int(line.strip())
                
                matrix.append(num)

    return matrix

def part1(ids, ranges):
    """
    Goes through each range for each id, and checks if it is in the range
    """
    count = 0
    is_fresh = False

    for id in ids:
        for range in ranges:
        
            if id >= range[0] and id <= range[1]:
                is_fresh = True

        if is_fresh:
            count += 1
            is_fresh = False
    
    return count

def add_to_set(set1,ran):
    current_set = set1
    for number in range(ran[0], ran[1]+1):
        if number not in current_set:
            current_set.add(number)
    
    return current_set

def part2(ranges):
    if not ranges:
        return 0

    # sort ranges by start
    ranges.sort(key=lambda x: x[0])

    total = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            # overlap or touching
            current_end = max(current_end, end)
        else:
            # finish previous range
            total += current_end - current_start + 1
            current_start, current_end = start, end

    # add last range
    total += current_end - current_start + 1

    print(total)
    return total

def main():
    print("Part 1:")
    part1(read_ids_into_array("input.txt"), read_ranges_into_array("input.txt"))

    print("Part 2:")
    part2(read_ranges_into_array("input.txt"))

if __name__ == "__main__":
    main()