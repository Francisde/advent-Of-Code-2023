import time
import sys

sys.setrecursionlimit(10000)

from utils.utils import print_2d

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

count = 0

field = []
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    row = [c for c in line_s]
    field.append(row)

print_2d(field)
marked_fields = set()

cache = dict()
def forward_solve_puzzle(input, current_x, current_y, steps):
    if "{}-{}-{}".format(current_y, current_x, steps) in cache.keys():
        return
    else:
        cache["{}-{}-{}".format(current_y, current_x, steps)] = 1
    if steps < 1:
        marked_fields.add((current_y, current_x))
        return

    else:
        # step north
        if current_y -1 >= 0:
            if input[current_y - 1][current_x] != "#":
                forward_solve_puzzle(input, current_x, current_y - 1, steps - 1)
        # step south
        if current_y + 1 < len(input):
            if input[current_y + 1][current_x] != "#":
                forward_solve_puzzle(input, current_x, current_y + 1, steps - 1)
        # step west
        if current_x - 1 >= 0:
            if input[current_y][current_x - 1] != "#":
                forward_solve_puzzle(input, current_x - 1, current_y, steps - 1)
        # step east
        if current_x + 1 < len(input[0]):
            if input[current_y][current_x + 1] != "#":
                forward_solve_puzzle(input, current_x + 1, current_y, steps - 1)


# find S
s = (0,0)
for i in range(len(field)):
    for j in range(len(field[0])):
        if field[i][j] == "S":
            s = (i,j)
print(s)
tic = time.time()
forward_solve_puzzle(field, s[1], s[0], 5000)
toc = time.time()
print(f'Completed in {toc - tic} seconds')
print(len(marked_fields))
print(marked_fields)