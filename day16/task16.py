import sys

sys.setrecursionlimit(10000)

file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0

game = []
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    row = []
    for character in line_s:
        row.append(character)
    game.append(row)

marked = []
direction_map = []
for row in game:
    marked_row = ["." for character in row]
    marked.append(marked_row)
    direction_row = [[] for character in row]
    direction_map.append(direction_row)


rules = {
    "EAST-\\": "SOUTH",
    "EAST-/": "NORTH",
    "EAST--": "EAST",
    "EAST-.": "EAST",
    "EAST-|": "NORTH-SOUTH",
    "WEST-\\": "NORTH",
    "WEST-/": "SOUTH",
    "WEST--": "WEST",
    "WEST-.": "WEST",
    "WEST-|": "NORTH-SOUTH",
    "NORTH-\\": "WEST",
    "NORTH-/": "EAST",
    "NORTH--": "EAST-WEST",
    "NORTH-.": "NORTH",
    "NORTH-|": "NORTH",
    "SOUTH-\\": "EAST",
    "SOUTH-/": "WEST",
    "SOUTH--": "EAST-WEST",
    "SOUTH-.": "SOUTH",
    "SOUTH-|": "SOUTH",
}

def follow_light(direction, current_x, current_y):
    #print("direction: {}, current_x: {}, current_y: {}".format(direction, current_x, current_y))
    # TODO check edges
    if current_x < 0 or current_y < 0:
        return
    if current_x >= len(game[0]):
        return
    if current_y >= len(game):
        return
    marked[current_y][current_x] = "#"
    if direction in direction_map[current_y][current_x]:
        return
    else:
        direction_map[current_y][current_x].append(direction)


    new_direction = ""
    if game[current_y][current_x] == "\\":
        new_direction = rules["{}-{}".format(direction, "\\")]
    elif game[current_y][current_x] == "/":
        new_direction = rules["{}-{}".format(direction, "/")]
    if game[current_y][current_x] == "-":
        new_direction = rules["{}-{}".format(direction, "-")]
    if game[current_y][current_x] == ".":
        new_direction = rules["{}-{}".format(direction, ".")]
    if game[current_y][current_x] == "|":
        new_direction = rules["{}-{}".format(direction, "|")]

    #print("current_marker: {}, new direction: {}".format(game[current_y][current_x], new_direction))

    if new_direction.count("EAST") == 1:
        follow_light("EAST", current_x + 1, current_y)
    if new_direction.count("WEST") == 1:
        follow_light("WEST", current_x - 1, current_y)
    if new_direction.count("NORTH") == 1:
        follow_light("NORTH", current_x, current_y - 1)
    if new_direction.count("SOUTH") == 1:
        follow_light("SOUTH", current_x, current_y + 1)


def print_map(input):
    for row in input:
        print(row)
    print()


marked_sum = 0
# from left side:
direction = "EAST"
current_x = 0
for i in range(len(game)):
    current_y = i
    marked = []
    direction_map = []
    for row in game:
        marked_row = ["." for character in row]
        marked.append(marked_row)
        direction_row = [[] for character in row]
        direction_map.append(direction_row)
    follow_light(direction, current_x, current_y)
    inner_sum = 0
    for row in marked:
        for character in row:
            if character == "#":
                inner_sum += 1
    print(inner_sum)
    if inner_sum > marked_sum:
        marked_sum = inner_sum

# from right side:
direction = "WEST"
current_x = len(game[0]) -1
for i in range(len(game)):
    current_y = i
    marked = []
    direction_map = []
    for row in game:
        marked_row = ["." for character in row]
        marked.append(marked_row)
        direction_row = [[] for character in row]
        direction_map.append(direction_row)
    follow_light(direction, current_x, current_y)
    inner_sum = 0
    for row in marked:
        for character in row:
            if character == "#":
                inner_sum += 1
    print(inner_sum)
    if inner_sum > marked_sum:
        marked_sum = inner_sum

# from bottom side:
direction = "NORTH"
current_y = len(game) -1
for i in range(len(game[0])):
    current_x = i
    marked = []
    direction_map = []
    for row in game:
        marked_row = ["." for character in row]
        marked.append(marked_row)
        direction_row = [[] for character in row]
        direction_map.append(direction_row)
    follow_light(direction, current_x, current_y)
    inner_sum = 0
    for row in marked:
        for character in row:
            if character == "#":
                inner_sum += 1
    print(inner_sum)
    if inner_sum > marked_sum:
        marked_sum = inner_sum

# from top side:
direction = "SOUTH"
current_y = 0
for i in range(len(game[0])):
    current_x = i
    marked = []
    direction_map = []
    for row in game:
        marked_row = ["." for character in row]
        marked.append(marked_row)
        direction_row = [[] for character in row]
        direction_map.append(direction_row)
    print("current_x {}, current_y: {}".format(current_x, current_y))
    follow_light(direction, current_x, current_y)
    inner_sum = 0
    for row in marked:
        for character in row:
            if character == "#":
                inner_sum += 1
    print(inner_sum)
    if inner_sum > marked_sum:
        marked_sum = inner_sum

marked = []
direction_map = []
for row in game:
    marked_row = ["." for character in row]
    marked.append(marked_row)
    direction_row = [[] for character in row]
    direction_map.append(direction_row)
print_map(marked)
follow_light("SOUTH", 3, 0)
print_map(marked)
print(marked_sum)