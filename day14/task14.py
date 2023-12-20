file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0
field = []

def print_field(field):
    for row in field:
        print(row)
    print()

def calc_load(field):
    result = 0
    for i in range(len(field)):
        rock_count = field[i].count("O")
        result += (rock_count * (len(field) - i))
    return result

def move_north(field):
    moved = True
    while moved:
        moved = False
        for i in range(1, len(field), 1):
            for j in range(len(field[0])):
                if field[i][j] == "O" and field[i - 1][j] == ".":
                    field[i][j] = "."
                    field[i - 1][j] = "O"
                    moved = True

def move_south(field):
    moved = True
    while moved:
        moved = False
        for i in range(len(field) -1, 0, -1):
            for j in range(len(field[0])):
                if field[i - 1][j] == "O" and field[i][j] == ".":
                    field[i - 1][j] = "."
                    field[i][j] = "O"
                    moved = True

def move_west(field):
    moved = True
    while moved:
        moved = False
        for i in range(1, len(field[0]), 1):
            for j in range(len(field)):
                if field[j][i - 1] == "." and field[j][i] == "O":
                    field[j][i - 1] = "O"
                    field[j][i] = "."
                    moved = True

def move_east(field):
    moved = True
    while moved:
        moved = False
        for i in range(len(field) -1, 0, -1):
            for j in range(len(field)):
                if field[j][i] == "." and field[j][i - 1] == "O":
                    field[j][i] = "O"
                    field[j][i - 1] = "."
                    moved = True

def rotate_field(field, count):
    results = dict()
    counter = 0
    while counter < count:
        counter += 1

        move_north(field)
        move_west(field)
        move_south(field)
        move_east(field)
        if str(field) in results:
            diff = counter - results[str(field)]
            print("{} + result: {} diff = {}".format(counter, results[str(field)], diff))
            while counter + diff < count - (2 * diff):
                counter += diff
        results[str(field)] = counter




# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    row = []
    for character in line_s:
        row.append(character)
    field.append(row)

field2 = field

print_field(field)
rotate_field(field, 1000000000)
print_field(field)
print(calc_load(field))

