file1 = open('input7.txt', 'r')
Lines1 = file1.readlines()

file2 = open('input12.txt', 'w')

count = 0

for line in Lines1:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))

    first_part = line_s.split(" ")[0]
    print(first_part)
    new_first_part = "{}?{}?{}?{}?{}".format(first_part, first_part, first_part, first_part, first_part)
    second_part = line_s.split(" ")[1]
    new_second_part = "{},{},{},{},{}".format(second_part, second_part, second_part, second_part, second_part)
    file2.write("{} {}\n".format(new_first_part, new_second_part))
