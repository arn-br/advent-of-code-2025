def read_ranges_into_array(filename):
    """
    Description:
        Reads the ranges from the text file to a 2D array

    Args:
        filename
    
    Returns:
        matrix: 2d array with ranges
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
    Description:
        Reads the ids from the text file to an array
    
    Args:
        filename
    
    Returns:
        matrix: an array with the ids
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
    Description:
        Goes through each range for each id, and checks if it is in the range

    Args:
        ids: array with ids
        ranges: array with ranges
    
    Returns:
        count: returns the count for valid ids
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

def part2(ranges):
    """
    Description:
        Goes through every range and calculates the total range

    Args:
        ranges: ranges from the file
    
    Returns:
        total: total number of available id count
    """
    ranges.sort(key=lambda x: x[0]) #sorting the ranges based on the start

    total = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1: #checking if the ranges overlap
            current_end = max(current_end, end)
        else:
            total += current_end - current_start + 1
            current_start, current_end = start, end

    total += current_end - current_start + 1

    return total

def main():
    print("Part 1:")
    part1(read_ids_into_array("input.txt"), read_ranges_into_array("input.txt"))

    print("Part 2:")
    part2(read_ranges_into_array("input.txt"))

if __name__ == "__main__":
    main()