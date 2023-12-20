file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0
appended_sum = 0
previous_sum = 0
def just_zero(input):
    for i in input:
        if i != 0:
            return False
    return True

# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    rows = []
    split_line = line_s.split(" ")
    current_row = [int(x) for x in split_line]
    print(current_row)
    rows.append(current_row)
    while not just_zero(current_row):
        new_row = []
        for i in range(len(current_row)-1):
            new_row.append(current_row[i + 1] - current_row[i])
        print(new_row)
        rows.append(new_row)
        current_row = new_row

    inner_sum = 0
    for i in range(len(rows)):
        print(rows[(len(rows) - 1) - i])
        inner_sum += rows[(len(rows) - 1) - i][len(rows[(len(rows) - 1) - i]) -1]
        print(inner_sum)
    appended_sum += inner_sum

    inner_sum = 0
    for i in range(len(rows)):
        print(rows[(len(rows) - 1) - i])
        inner_sum = rows[(len(rows) - 1) - i][0] - inner_sum
        print(inner_sum)
    previous_sum += inner_sum

print("appended_sum: {}".format(appended_sum))
print("previous_sum: {}".format(previous_sum))