from utils.utils import print_2d

file1 = open('input7.txt', 'r')
Lines = file1.readlines()

count = 0

steps = {
    "|N": "S",
    "|S": "N",
    "-W": "O",
    "-O": "W",
    "LN": "O",
    "LO": "N",
    "JW": "N",
    "JN": "W",
    "7W": "S",
    "7S": "W",
    "FS": "O",
    "FO": "S"
}

def is_loop(field, starting_row, starting_col, come_from):
    passed_tiles = []

    current_tile = (starting_row, starting_col)
    step_count = 0
    come_from = come_from
    while True:
        next_tile = ()
        try:

            print("step {}, from {}{}, direction: {}".format(step_count, current_tile[0], current_tile[1], steps["{}{}".format(field[current_tile[0]][current_tile[1]], come_from)]))
        except KeyError:
            return (-1, None)
        direction = steps["{}{}".format(field[current_tile[0]][current_tile[1]], come_from)]

        if direction == "N":
            next_tile = (current_tile[0] - 1, current_tile[1])
            come_from = "S"
        elif direction == "S":
            next_tile = (current_tile[0] + 1, current_tile[1])
            come_from = "N"
        elif direction == "W":
            next_tile = (current_tile[0], current_tile[1] - 1)
            come_from = "O"
        elif direction == "O":
            next_tile = (current_tile[0], current_tile[1] + 1)
            come_from = "W"
        step_count += 1
        current_tile = next_tile
        if current_tile[0] == starting_row and current_tile[1] == starting_col:
            passed_tiles.append(current_tile)
            return (step_count, passed_tiles)
        elif current_tile in passed_tiles or field[current_tile[0]][current_tile[1]] == ".":
            return (-1, None)
        else:
            passed_tiles.append(current_tile)



game_field = []
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    row = []
    for character in line_s:
        row.append(character)
    game_field.append(row)

row_s = 0
col_s = 0
# find S
for i in range(len(game_field)):
    for j in range(len(game_field[i])):
        if game_field[i][j] == "S":
            row_s = i
            col_s = j
            break

print_2d(game_field)
combinations = [("|N", "|S"), ("-W", "-O"), ("LN", "LO"), ("JW", "JN"), ("7W", "7S"), ("FS", "FO")]
longest_comb = []
lengths = []
for combination in combinations:
    inner_comb = combination[0]
    game_field[row_s][col_s] = inner_comb[0]
    loop_length1 = is_loop(game_field, row_s, col_s, inner_comb[1])[0]
    inner_comb = combination[1]
    game_field[row_s][col_s] = inner_comb[0]
    loop_length2 = is_loop(game_field, row_s, col_s, inner_comb[1])[0]
    if loop_length1 == loop_length2:
        if loop_length1 > 0:
            print(loop_length1)
            longest_comb.append(combination)
            lengths.append(int(loop_length1 / 2))
print("longest_comb: {}".format(longest_comb))
print(lengths)

print_2d(game_field)

marking_board = []
for row in game_field:
    marking_board.append(["." for i in row])
print_2d(marking_board)

passed_tiles = []

current_tile = (row_s, col_s)
step_count = 0
come_from = longest_comb[0][0][1]
print("initial come-from {}".format(come_from))
game_field[row_s][col_s] = longest_comb[0][0][0]
# TODO max steps
while step_count < 20000:
    next_tile = ()
    direction = steps["{}{}".format(game_field[current_tile[0]][current_tile[1]], come_from)]

    marking_board[current_tile[0]][current_tile[1]] = "M"

    if direction == "N":
        next_tile = (current_tile[0] - 1, current_tile[1])
        come_from = "S"
        try:
            if game_field[current_tile[0]][current_tile[1] - 1] == ".":
                marking_board[current_tile[0]][current_tile[1] - 1] = "O"
            if game_field[current_tile[0]][current_tile[1] + 1] == ".":
                marking_board[current_tile[0]][current_tile[1] + 1] = "I"
        except IndexError:
            pass
    elif direction == "S":
        next_tile = (current_tile[0] + 1, current_tile[1])
        come_from = "N"
        try:
            if game_field[current_tile[0]][current_tile[1] - 1] == ".":
                marking_board[current_tile[0]][current_tile[1] - 1] = "I"
            if game_field[current_tile[0]][current_tile[1] + 1] == ".":
                marking_board[current_tile[0]][current_tile[1] + 1] = "O"
        except IndexError:
            pass
    elif direction == "W":
        next_tile = (current_tile[0], current_tile[1] - 1)
        come_from = "O"
        try:
            if game_field[current_tile[0] - 1][current_tile[1]] == ".":
                marking_board[current_tile[0] - 1][current_tile[1]] = "I"
            if game_field[current_tile[0] + 1][current_tile[1]] == ".":
                marking_board[current_tile[0] + 1][current_tile[1]] = "O"
        except IndexError:
            pass
    elif direction == "O":
        next_tile = (current_tile[0], current_tile[1] + 1)
        come_from = "W"
        try:
            if game_field[current_tile[0] - 1][current_tile[1]] == ".":
                marking_board[current_tile[0] - 1][current_tile[1]] = "O"
            if game_field[current_tile[0] + 1][current_tile[1]] == ".":
                marking_board[current_tile[0] + 1][current_tile[1]] = "I"
        except IndexError:
            pass
    step_count += 1
    current_tile = next_tile

# mark edges with O
for i in range(len(marking_board[0])):
    if marking_board[0][i] == ".":
        marking_board[0][i] = "B"
for i in range(len(marking_board[len(marking_board) - 1])):
    if marking_board[len(marking_board) - 1][i] == ".":
        marking_board[len(marking_board) - 1][i] = "B"
for row in marking_board:
    if row[0] == ".":
        row[0] = "B"
    if row[len(row) -1] == ".":
        row[len(row) -1] = "B"

# expand markings
marked = True
while marked:
    marked = False
    for i in range(len(marking_board)):
        for j in range(len(marking_board[i])):
            if marking_board[i][j] == "." and (marking_board[i + 1][j] == "I" or marking_board[i -1][j]== "I" or marking_board[i][j + 1]== "I" or marking_board[i][j - 1]== "I" or marking_board[i +1][j +1] == "I" or marking_board[i + 1][j - 1]== "I" or marking_board[i -1 ][j + 1]== "I" or marking_board[i -1][j -1]== "I"):
                marking_board[i][j] = "I"
                marked = True
    for i in range(len(marking_board)):
        for j in range(len(marking_board[i])):
            if marking_board[i][j] == "." and (marking_board[i + 1][j] == "O" or marking_board[i -1][j]== "O" or marking_board[i][j + 1]== "O" or marking_board[i][j - 1]== "O" or marking_board[i +1][j +1] == "O" or marking_board[i + 1][j - 1]== "O" or marking_board[i -1 ][j + 1]== "O" or marking_board[i -1][j -1]== "O"):
                marking_board[i][j] = "O"
                marked = True

print_2d(marking_board)
marked = 0
for i in range(len(marking_board)):
    for j in range(len(marking_board[i])):
        if marking_board[i][j] == "I":
            marked += 1
print(marked)
marked = 0
for i in range(len(marking_board)):
    for j in range(len(marking_board[i])):
        if marking_board[i][j] == "O":
            marked += 1
print(marked)
marked = 0
for i in range(len(marking_board)):
    for j in range(len(marking_board[i])):
        if marking_board[i][j] == ".":
            marked += 1
print(marked)