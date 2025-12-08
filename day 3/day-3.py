def int_to_list(int1):
    k = list(map(int, str(int1)))
    return k


def find_max_two(l1):
    num1 = max(l1[: (len(l1)-1)]) #find the max number in the listm excluding the last digit
    
    index2 = l1.index(num1)

    num2 = max(l1[(index2+1):]) #find the second max number, following digits from the first max

    res = int(str(num1) + str(num2))

    return res

def first_twelve(l1: list):
    res = ""
    num1 = max(l1[:(len(l1) - 10)]) #find the max digit ( 11 digits at the end excluded)
    index1 = l1.index(num1)

    for n in range(index1): #change every digit to 0 until to the  max digit
        l1[n] = 0
    l1[index1] = 0

    res = str(num1) #add the digit to the result

    for i in range(11): #follow the same logic here, until we have 12 digits
        
        num1 = max(l1[index1:(len(l1) - 10 + i)])
        index1 = l1.index(num1)

        for n in range(index1):
            l1[n] = 0
        l1[index1] = 0
        
        res += str(num1)

    #print(res)
    return int(res)

def part1():
    res = 0

    with open("input.txt", "r") as f:
        f.seek(0)
        lines = f.readlines()

        for line in lines:
            text_line = line.strip()
            k = int(text_line)
            res += find_max_two(int_to_list(k))
    
    print(res)

def part2():
    res = 0

    with open("input.txt", "r") as f:
        f.seek(0)
        lines = f.readlines()

        for line in lines:
            text_line = line.strip()
            k = int(text_line)
            res += first_twelve(int_to_list(k))
    
    print(res)

def main():
    print("Part 1:")
    part1()

    print("\nPart 2:")
    part2()

if __name__ == "__main__":
    main()