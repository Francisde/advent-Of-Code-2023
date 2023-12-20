import numpy as np

file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0

field_length = 10
field_height = 10

moves = []
moves_2 = []
def print_game(game):
    for row in game:
        print(row)

x_points = []
y_points = []


# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    split_line = line_s.split(" ")
    moves.append((split_line[0], int(split_line[1])))
    if split_line[0] == "R":
        field_length += int(split_line[1])
    if split_line[0] == "D":
        field_height += int(split_line[1])

    print(int(split_line[2][2:7], 16))

print("field_length")
print(field_length)
print("field_height")
print(field_height)
game_field = []
for i in range(field_height):
    game_field.append(["." for x in range(field_length)])

def dig_edges(game, moves):
    current_x = 0
    current_y = 0
    for move in moves:
        if move[0] == "R":
            for i in range(current_x, current_x + move[1] + 1, 1):
                game[current_y][i] = "#"
                if game[current_y + 1][i] == ".":
                    game[current_y + 1][i] = "I"
            current_x = current_x + move[1]
        elif move[0] == "D":
            for i in range(current_y, current_y + move[1] + 1, 1):
                game[i][current_x] = "#"
                if game[i][current_x - 1] == ".":
                    game[i][current_x - 1] = "I"
            current_y = current_y + move[1]
        elif move[0] == "L":
            print("L")
            for i in range(current_x - move[1] , current_x, 1):
                print(i)
                game[current_y][ i] = "#"
            current_x = current_x - move[1]
        elif move[0] == "U":
            for i in range(current_y - move[1] , current_y, 1):
                game[i][current_x] = "#"
            current_y = current_y - move[1]
print(moves)
#print_game(game_field)

dig_edges(game_field, moves)
print_game(game_field)
changed = True
while changed:
    changed = False
    for i in range(len(game_field)):
        for j in range(len(game_field[0])):
            if game_field[i][j] == "I":
                if i < len(game_field)-1 and game_field[i + 1][j] == ".":
                    game_field[i + 1][j] = "I"
                    changed = True
                if game_field[i - 1][j] == ".":
                    game_field[i - 1][j] = "I"
                    changed = True
                if j < len(game_field[0])- 1:
                    if game_field[i][j + 1] == ".":
                        game_field[i][j + 1] = "I"
                        changed = True
                if game_field[i ][j - 1] == ".":
                    game_field[i][j - 1] = "I"
                    changed = True

print_game(game_field)

for i in range(len(game_field)):
    for j in range(len(game_field[0])):
        if game_field[i][j] == "I":
            game_field[i][j] = "#"

counter = 0
for i in range(len(game_field)):
    for j in range(len(game_field[0])):
        if game_field[i][j] == "#":
            counter += 1
print("digged square meters: {}".format(counter))

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

current_x = 0
current_y = 0
x_points.append(current_x)
y_points.append(current_y)
correction_term = 0
for i in range(len(moves) -1):
    if moves[i][0] == "D" and moves[i + 1][0] == "L":
        correction_term += 1
    if moves[i][0] == "L" and moves[i + 1][0] == "D":
        correction_term -= 1
for move in moves:
    if move[0] == "R":
        current_x += move[1]
    elif move[0] == "D":
        correction_term += move[1]
        current_y += move[1]
    elif move[0] == "L":
        correction_term += move[1]
        current_x = current_x - (move[1] )
    elif move[0] == "U":
        current_y = current_y - (move[1])
    print("X: {}, Y: {}".format(current_x, current_y))
    x_points.append(current_x)
    y_points.append(current_y)
print(y_points)
points = []
points_string = ""
for i in range(len(x_points)):
    points.append([x_points[i], y_points[i]])
    points_string += str(x_points[i])
    points_string += ","
    points_string += str(y_points[i])
    points_string += " "
# vertices = np.concatenate((points, points[:1]), axis=0)
# sides = np.linalg.norm(np.diff(vertices, axis=0), axis=-1)
# print(sides)
# sum_sides = np.sum(sides)
# print(sum_sides)

print(PolyArea(x_points, y_points))

def find_area_perim(array):
    a = 0
    p = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        p += abs((x-ox)+(y-oy)*1j)
        ox,oy = x,y
    return a/2,p

def find_area(array):
    a = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        ox,oy = x,y
    return a/2

print(find_area_perim(points))
print("correction: {}".format(correction_term))
print("total: {}".format(int(PolyArea(x_points, y_points))+ correction_term))