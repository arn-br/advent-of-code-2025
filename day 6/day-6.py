def read_columns(filename):
    columns = []

    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue
            
            values = line.split()

            if not columns:
                columns = [[] for _ in values]           

            for i, value in enumerate(values):
                if value in ["+", "*"]:
                    columns[i].append(value)
                else:
                    columns[i].append(int(value))

    return columns

def read_columns2(filename):
    columns = []
    
    with open(filename, "r") as f:
        lines = f.readlines()
        
    len_cols = len(lines[0])
    len_rows = len(lines)

    col = []
    for i in range(len_cols):
        value = ""
        for n in range(len_rows-1):
            current_row = lines[n]
            current_character = current_row[i]
            value += str(current_character) #creating the number top to bottom

        #if the value is made of spaces, enter a new column
        if value.strip() != "": 
            col.append(int(value))
        else:
            columns.append(col)
            col = []

    operators = str(lines[len_rows-1])
    operators = operators.replace(" ", "")
    for m in range(len(operators)):
        columns[m].append(operators[m])

    return columns

def calculate_column(columns):
    results = []
    for column in columns:
        numbers = column[:-1]
        op = column[-1]

        if op == "*":
            res = 1
            for n in numbers:
                res *= n
        elif op == "+":
            res = sum(numbers)
        
        results.append(res)

    return results

def transform_nums(columns):
    print(columns)
    for column in columns:
        numbers = column[:-1]
        op = column[-1]

        new_nums = []
        copied = numbers[:]

        while copied:
            new_number = ""
            nexts = []

            for n in copied:
                new_number += str(n % 10)
                n //= 10
                if n > 0:
                    nexts.append(n)
            
            new_nums.append(int(new_number))
            copied = nexts


        column[:] = new_nums +[op]

    print(columns)            
    return columns

def part1(filename):
    total = sum(calculate_column(read_columns(filename)))

    print(total)

def part2(filename):
    total = sum(calculate_column(read_columns2(filename)))

    print(total)

def main():
    #print("Part 1:")
    #part1("test.txt")

    print("Part 2:")
    part2("input.txt")

if __name__ == "__main__":
    main()