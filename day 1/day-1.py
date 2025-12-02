def part1_rotate_left(num: int, k: int) -> int:
    return (num -k) % 100

def part1_rotate_right(num: int, k: int) -> int:
    return (num + k) % 100

def click_count_left(num :int, k: int):
    value = num - k
    res = value % 100
    
    j = 0
    if value < -100:
        j += value // -100
        value = value % -100

    if value < 0:
        j += 1 

    if num == 0:
        j -= 1
    
    return j

def click_count_right(num: int, k: int):
    value = (num + k)
    res = value % 100
    
    j = 0 
    if value > 99:
        j += value // 100
        value = value % 100

    if value > 99 :
        j += 1 

    if res == 0:
        j -= 1  
    
    return j


def part1() -> int:
    file_path = "input.txt" 

    try:
        number = 50
        key = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            file.seek(0)
            lines = file.readlines()
            for line in lines:
                text_line = line.strip()
                k = int(text_line[1:])

                if "L" in text_line:
                    number = part1_rotate_left(number, k)
                else:
                    number = part1_rotate_right(number, k)

                if number == 0:
                    key += 1
        
        return key

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def part2() -> int:
    file_path = "input.txt" 
    

    try:
        number = 50
        key = 0
        
        with open(file_path, 'r', encoding='utf-8') as file:
            file.seek(0)
            lines = file.readlines()
            
            for line in lines:
                text_line = line.strip()
                k = int(text_line[1:])

                if "L" in text_line:
                    val1 = click_count_left(number, k)
                    number = part1_rotate_left(number, k)
                else:
                    val1= click_count_right(number, k)
                    number = part1_rotate_right(number, k)
                
                if number == 0:
                    key += 1
                
                key += val1

        return key
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()
