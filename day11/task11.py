file1 = open('input1.txt', 'r')
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
new_space = []
changes = True
changed = 0
while changes:
    changes = False
    for i in range(changed, len(space[0]), 1):
        galaxy = False
        for j in range(len(space)):
            if space[j][i] == "#":
                galaxy = True
                break
        if not galaxy:
            changed = i+2
            print(i)
            for j in range(len(space)):
                space[j].insert(i, ".")
                changes = True
            break

changes = True
changed = 0
while changes:
    changes = False
    for i in range(changed, len(space), 1):
        if "#" not in space[i]:
            galaxy = True
            changed = i+2
            print(i)
            changes = True
            space.insert(i, space[i])
            break


print_space(space)

list_of_galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == "#":
            list_of_galaxies.append((i,j))
print(list_of_galaxies)

path_sum = 0
for i in list_of_galaxies:
    for j in list_of_galaxies:
        path = (abs(i[0] - j[0]) + abs(i[1] - j[1]))
        path_sum += path
        print("I: {} , J: {}, E_col: {}, E_row: {}, path: {}".format(i, j, 0, 0, path))

print(int(path_sum/2))


