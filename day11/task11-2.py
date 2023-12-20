file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0

space = []
def print_space(input):
    for row in input:
        print(row)
    print()

# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    row = []
    for character in line_s:
        row.append(character)
    space.append(row)

print_space(space)

# expand galaxy

for i in range(len(space[0])):
    galaxy = False
    for j in range(len(space)):
        if space[j][i] == "#":
            galaxy = True
            break
    if not galaxy:
        for j in range(len(space)):
            space[j][i] = "E"

for i in range(len(space)):
    if "#" not in space[i]:
        for j in range(len(space[i])):
            space[i][j] = "E"


print_space(space)

expansion_factor = 999999


list_of_galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == "#":
            list_of_galaxies.append((i,j))
print(list_of_galaxies)

path_sum = 0
for i in list_of_galaxies:
    for j in list_of_galaxies:
        # count E between
        e_counter_row = 0
        e_counter_col = 0
        left_galaxy = None
        right_galaxy = None
        upper_galaxy = None
        lower_galaxy = None
        if i[1] < j[1]:
            left_galaxy = i
            right_galaxy = j
        else:
            left_galaxy = j
            right_galaxy = i
        if i[0] < j[0]:
            upper_galaxy = i
            lower_galaxy = j
        else:
            upper_galaxy = j
            lower_galaxy = i

        for count in range(left_galaxy[1], right_galaxy[1], 1):
            if space[0][count] == "E":
                e_counter_row += 1
        for count in range(upper_galaxy[0], lower_galaxy[0], 1):
            if space[count][0] == "E":
                e_counter_col += 1
        path = (((abs(i[0] - j[0]) + e_counter_col * expansion_factor) + (abs(i[1] - j[1]) + e_counter_row * expansion_factor )))
        print("I: {} , J: {}, E_col: {}, E_row: {}, path: {}".format(i, j, e_counter_col, e_counter_row, path))
        path_sum += path

print(int(path_sum/2))


