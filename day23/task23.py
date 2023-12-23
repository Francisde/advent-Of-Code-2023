from utils.utils import print_2d
import sys

sys.setrecursionlimit(7000)

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

count = 0

hiking_map = []
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    row = [c for c in line_s]
    hiking_map.append(row)

print_2d(hiking_map)

start_point = (0, 1)
end_point = (len(hiking_map) - 1, len(hiking_map[0]) - 2)

print(start_point)
print(end_point)

global_paths = []
def find_longest_path(game_field, current_position, end_position, steps):
    global global_paths
    paths = []
    #result = []
    if current_position == end_position:
        paths.append(steps)
        global_paths.append(steps)
        return paths
    if game_field[current_position[0]][current_position[1]] == ".":
        game_field[current_position[0]][current_position[1]] = "O"
        # go south
        if current_position[0] + 1 <= len(game_field) and game_field[current_position[0] + 1][current_position[1]] != "#":
            result = find_longest_path(game_field, (current_position[0] + 1, current_position[1]), end_position, steps + 1)
        # go north
        if current_position[0] - 1 >= 0 and game_field[current_position[0] - 1][current_position[1]] != "#":
            result = find_longest_path(game_field, (current_position[0] - 1, current_position[1]), end_position, steps + 1)
        # go west
        if current_position[1] - 1 >= 0 and game_field[current_position[0]][current_position[1] - 1] != "#":
            result = find_longest_path(game_field, (current_position[0], current_position[1] - 1), end_position, steps + 1)
        # go east
        if current_position[1] + 1 <= len(game_field[0]) and game_field[current_position[0]][current_position[1] + 1] != "#":
            result = find_longest_path(game_field, (current_position[0], current_position[1] + 1), end_position, steps + 1)
        print(result)
        game_field[current_position[0]][current_position[1]] = "."
    if game_field[current_position[0]][current_position[1]] == ">":
        game_field[current_position[0]][current_position[1]] = "O"
        # go east
        if current_position[1] + 1 <= len(game_field[0]) and game_field[current_position[0]][current_position[1] + 1] != "#":
            result = find_longest_path(game_field, (current_position[0], current_position[1] + 1), end_position, steps + 1)
        game_field[current_position[0]][current_position[1]] = ">"
    if game_field[current_position[0]][current_position[1]] == "<":
        game_field[current_position[0]][current_position[1]] = "O"
        # go west
        if current_position[1] - 1 >= 0 and game_field[current_position[0]][current_position[1] - 1] != "#":
            result = find_longest_path(game_field, (current_position[0], current_position[1] - 1), end_position, steps + 1)
        game_field[current_position[0]][current_position[1]] = "<"
    if game_field[current_position[0]][current_position[1]] == "v":
        game_field[current_position[0]][current_position[1]] = "O"
        # go south
        if current_position[0] + 1 <= len(game_field) and game_field[current_position[0] + 1][current_position[1]] != "#":
            result = find_longest_path(game_field, (current_position[0] + 1, current_position[1]), end_position, steps + 1)
        game_field[current_position[0]][current_position[1]] = "v"
    if game_field[current_position[0]][current_position[1]] == "^":
        game_field[current_position[0]][current_position[1]] = "O"
        # go north
        if current_position[0] - 1 >= 0 and game_field[current_position[0] - 1][current_position[1]] != "#":
            result = find_longest_path(game_field, (current_position[0] - 1, current_position[1]), end_position, steps + 1)
        game_field[current_position[0]][current_position[1]] = "^"
    for res in result:
        paths.append(res)
    return paths


result = find_longest_path(hiking_map, start_point, end_point, 0)

global_paths.sort(reverse=True)
print("global paths: {}".format(global_paths))

# part 2
for i in range(len(hiking_map)):
    for j in range(len(hiking_map[0])):
        if hiking_map[i][j] != "#":
            hiking_map[i][j] = "."

global_paths = []
result = find_longest_path(hiking_map, start_point, end_point, 0)

global_paths.sort(reverse=True)
print("global paths: {}".format(global_paths))