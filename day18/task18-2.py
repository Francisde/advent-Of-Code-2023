import numpy as np

file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0

moves = []


x_points = []
y_points = []


# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    split_line = line_s.split(" ")
    #moves.append((split_line[0], int(split_line[1])))
    value = int(split_line[2][2:7], 16)
    direction_int = int(split_line[2][7:8], 16)
    direction = ""
    if direction_int == 0:
        direction = "R"
    if direction_int == 1:
        direction = "D"
    if direction_int == 2:
        direction = "L"
    if direction_int == 3:
        direction = "U"
    moves.append((direction, value))

    print(int(split_line[2][2:7], 16))
    print(int(split_line[2][7:8], 16))


print(moves)
changed = True

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
    # print("X: {}, Y: {}".format(current_x, current_y))
    x_points.append(current_x)
    y_points.append(current_y)

print(PolyArea(x_points, y_points))

print("correction: {}".format(correction_term))
print("total: {}".format(int(PolyArea(x_points, y_points))+ correction_term))