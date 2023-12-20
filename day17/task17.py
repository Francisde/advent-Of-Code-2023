import sys
import time

sys.setrecursionlimit(1000000)

file1 = open('input3.txt', 'r')
Lines = file1.readlines()

count = 0

game_field = []
all_ready_stepped = []
tic = time.time()
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    row = []
    row_s = []
    for character in line_s:
        row.append(int(character))
        row_s.append(False)
    game_field.append(row)
    all_ready_stepped.append(row_s)

minimum_length = -1

def reset_allready_steped():
    global all_ready_stepped
    all_ready_stepped = []
    for row in game_field:
        row_s = []
        for character in row:
            row_s.append(False)
        all_ready_stepped.append(row_s)

def find_minimum_path(current_y, current_x, direction, steps, path_length):
    global minimum_length
    max_steps = 2
    # check borders
    if current_y < 0 or current_x < 0:
        return
    if current_y >= len(game_field) or current_x >= len(game_field[0]):
        return
    if all_ready_stepped[current_y][current_x]:
        return
    else:
        all_ready_stepped[current_y][current_x] = True
    if current_y == len(game_field) -1 and current_x == len(game_field[0]) -1:
        if path_length < minimum_length or minimum_length == -1:
            minimum_length = path_length
            print("ret-1")
            print(path_length)
        all_ready_stepped[current_y][current_x] = False
        return
    elif (path_length > minimum_length) and minimum_length != -1:
        #print("ret-2")
        all_ready_stepped[current_y][current_x] = False
        return

    path_length += game_field[current_y][current_x]
    if direction == "NORTH":
        if steps < max_steps:
            find_minimum_path(current_y - 1, current_x, "NORTH", steps + 1, path_length)
        find_minimum_path(current_y, current_x - 1, "WEST", 0, path_length)
        find_minimum_path(current_y, current_x + 1, "EAST", 0, path_length)
    elif direction == "EAST":
        if steps < max_steps:
            find_minimum_path(current_y, current_x + 1, "EAST", steps + 1, path_length)
        find_minimum_path(current_y -1, current_x , "NORTH", 0, path_length)
        find_minimum_path(current_y + 1, current_x , "SOUTH", 0, path_length)
    elif direction == "SOUTH":
        if steps < max_steps:
            find_minimum_path(current_y + 1, current_x, "SOUTH", steps + 1, path_length)
        find_minimum_path(current_y, current_x - 1, "WEST", 0, path_length)
        find_minimum_path(current_y, current_x + 1, "EAST", 0, path_length)
    if direction == "WEST":
        if steps < max_steps:
            find_minimum_path(current_y, current_x - 1, "WEST", steps + 1, path_length)
        find_minimum_path(current_y -1, current_x , "NORTH", 0, path_length)
        find_minimum_path(current_y + 1, current_x , "SOUTH", 0, path_length)

    path_length -= game_field[current_y][current_x]
    all_ready_stepped[current_y][current_x] = False

# start
# find_minimum_path(0, 0, "EAST", 0, 0)
find_minimum_path(0, 0, "SOUTH", 0, 0)
reset_allready_steped()
print("reset")
find_minimum_path(0, 0, "EAST", 0, 0)
print(minimum_length)
toc = time.time()
print(f'Completed in {toc - tic} seconds')