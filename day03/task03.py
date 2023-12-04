file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0
sum = 0
input_array = []


class Gear:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        if self.row == other.row and self.col == other.col:
            return True
        return False

    def __str__(self):
        return "gear row: {}, col: {}".format(self.row, self.col)

class Number_Gear_Pairs:
    def __init__(self, number, gear_list):
        self.number = number
        self.gear_list = gear_list

def validate_number(left, right, row):
    # check left
    if left > 0:
        if input_array[row][left - 1] != ".":
            return True
    # check right:
    if right < len(input_array[row]) -1:
        if input_array[row][right + 1] != ".":
            return True
    # check top row
    if row > 0:
        for i in range(left, right + 1, 1):
            if input_array[row - 1][i] != "." and not input_array[row - 1][i].isdigit():
                return True
    # check bottom row
    if row < len(input_array) -1:
        for i in range(left, right + 1, 1):
            if input_array[row + 1][i] != "." and not input_array[row + 1][i].isdigit():
                return True
    # check diagonal left
    if left > 0:
        # check top
        if row > 0:
            if input_array[row - 1][left -1] != "." and not input_array[row - 1][ left -1].isdigit():
                return True
        # check bottom
        if row < len(input_array) -1:
            if input_array[row + 1][left -1] != "." and not input_array[row + 1][ left -1].isdigit():
                return True
    # check diagonal right
    if right < len(input_array[row]) -1:
        # check top
        if row > 0:
            if input_array[row - 1][right + 1] != "." and not input_array[row - 1][right + 1].isdigit():
                return True
        # check bottom
        if row < len(input_array) -1:
            if input_array[row + 1][right + 1] != "." and not input_array[row + 1][right + 1].isdigit():
                return True
    return False

def adjacent_to_gear(left, right, row):
    gear_list = []
    # check left
    if left > 0:
        if input_array[row][left - 1] == "*":
            gear_list.append(Gear(row, left -1))
    # check right:
    if right < len(input_array[row]) - 1:
        if input_array[row][right + 1] == "*":
            gear_list.append(Gear(row, right + 1))
    # check top row
    if row > 0:
        for i in range(left, right + 1, 1):
            if input_array[row - 1][i] == "*":
                gear_list.append(Gear(row - 1, i))
    # check bottom row
    if row < len(input_array) -1:
        for i in range(left, right + 1, 1):
            if input_array[row + 1][i] == "*":
                gear_list.append(Gear(row + 1, i))
    # check diagonal left
    if left > 0:
        # check top
        if row > 0:
            if input_array[row - 1][left -1] == "*":
                gear_list.append(Gear(row - 1, left - 1))
        # check bottom
        if row < len(input_array) -1:
            if input_array[row + 1][left -1] == "*":
                gear_list.append(Gear(row + 1, left - 1))
    # check diagonal right
    if right < len(input_array[row]) -1:
        # check top
        if row > 0:
            if input_array[row - 1][right + 1] == "*":
                gear_list.append(Gear(row - 1, right + 1))
        # check bottom
        if row < len(input_array) -1:
            if input_array[row + 1][right + 1] == "*":
                gear_list.append(Gear(row + 1, right + 1))
    return gear_list

# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    input_row = []
    for character in line_s:
        input_row.append(character)
    input_array.append(input_row)
print(input_array)

number_gear_pair_list = []

for counter_outer in range(len(input_array)):
    startindex = 0
    counter_inner = 0
    while counter_inner < len(input_array[counter_outer]):
        if input_array[counter_outer][counter_inner].isdigit():
            right_border = counter_inner + 1
            number_string = input_array[counter_outer][counter_inner]
            while right_border < len(input_array[counter_outer]):
                if input_array[counter_outer][right_border].isdigit():
                    number_string += input_array[counter_outer][right_border]
                    right_border += 1
                else:
                    break
            print("number: {}, valid: {}".format(number_string, validate_number(counter_inner, right_border -1, counter_outer)))
            if validate_number(counter_inner, right_border-1, counter_outer):
                sum += int(number_string)
                number_gear_pair_list.append(Number_Gear_Pairs(int(number_string), adjacent_to_gear(counter_inner, right_border-1, counter_outer)))
            counter_inner = right_border
        counter_inner += 1

print("sum: {}".format(sum))

gear_ratio_sum = 0
list_of_gears = []
for value in number_gear_pair_list:
    for gear in value.gear_list:
        if gear not in list_of_gears:
            list_of_gears.append(gear)
for gear in list_of_gears:
    print(gear)
    # find adjacent numbers
    adjacent_numbers = []
    for value in number_gear_pair_list:
        for value_gear in value.gear_list:
            if value_gear == gear:
                adjacent_numbers.append(value.number)
    print(adjacent_numbers)
    if len(adjacent_numbers) == 2:
        gear_ratio_sum += (adjacent_numbers[0] * adjacent_numbers[1])

print("gear ratio: {}".format(gear_ratio_sum))