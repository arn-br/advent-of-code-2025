def generate_invalid_in_range_p1(low, high):
    results = []
    
    low_len = len(str(low)) #digits for the lowest id
    high_len = len(str(high)) #digits for the highest id

    #calculating the smallest number to double, i.e. if num_min = 20, the first number to test will be 2020
    if (low_len % 2) == 1 :
        low_len += 1
        half_low_len = int(low_len/2)
        num_min = "1" + "0" * (half_low_len + 1)
        num_min = num_min[0:half_low_len] 
    else:
        half_low_len = int(low_len/2)
        string1 = str(low)
        num_min = string1[0:half_low_len]

    
    max_num = "9" * (half_low_len+1) #calculating the max number to be the half
    for i in range(int(num_min), int(max_num)):
        num = str(i) * 2

        if int(num) > high:
            break

        if int(num) >= low and int(num) <= high :
            results.append(int(num))

    return results

def part_1():
    res = 0

    with open("input2.txt", "r") as f:
        contents = f.read()

    ranges = [r.strip() for r in contents.split(",")]

    for r in ranges:
        if "-" in r:
            start, end = r.split("-")
            start = int(start.strip())
            end = int(end.strip())
    
            res += sum(generate_invalid_in_range_p1(start, end))
    
    print(res)

def generate_invalid_in_range_p2(low, high):
    results2 = {0}


    low_len = len(str(low))
    high_len = len(str(high))

    if (low_len % 2) == 1 : 
        half_low_len = int(low_len/2)
    else:
        half_low_len = int(low_len/2)
    
    if (high_len % 2) == 1:
        high_len += 1

            
    max_num = "9" * (half_low_len +1)
    
    for i in range((int(max_num))):
        len1 = len(str(i))

        if len1 == 1:
            num = str(i) * low_len
            if int(num) >= low and int(num) <= high and len(num)>1 :
                results2.add(int(num))

            num2 = str(i) * len(str(high))
            if int(num2) >= low and int(num2) <= high :
                results2.add(int(num2))
            
        elif len1 != high_len:
            len2 = (high_len // len1)
            
            for n in range(2, len2+1):
                num = str(i) * n
                if int(num) >= low and int(num) <= high :
                    results2.add(int(num))
    
    return sorted(results2)

def part_2():
    res = 0

    with open("input2.txt", "r") as f:
        contents = f.read()

    ranges = [r.strip() for r in contents.split(",")]

    for r in ranges:
        if "-" in r:
            start, end = r.split("-")
            start = int(start.strip())
            end = int(end.strip())
            res += sum(generate_invalid_in_range_p2(start, end))
    
    print(res)


def main():
    part_1()
    part_2()
    

if __name__ == "__main__":
    main()
