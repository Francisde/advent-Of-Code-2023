file1 = open('input12.txt', 'r')
Lines1 = file1.readlines()

file2 = open('output2_new.txt', 'r')
Lines2 = file2.readlines()

count = 0
solved = []
unsolved = []
# Strips the newline character
for line in Lines2:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    split_s = line_s.split(" : ")
    split_s1 = split_s[0]
    split_s2 = split_s[1]
    print(split_s2)
    split_s2 = split_s2.replace("[", "").replace("]", "").replace(" ", "")
    print(split_s2)

    split_s = "{} {}".format(split_s1, split_s2)
    print(split_s)
    solved.append(split_s)

count = 0
for line in Lines1:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    split_s = line_s
    print(split_s)
    if split_s in solved:
        pass
    else:
        unsolved.append(line_s)

print(len(solved))
print(len(unsolved))

file3 = open("input9.txt", 'w')
for row in unsolved:
    file3.write(row)
    file3.write("\n")