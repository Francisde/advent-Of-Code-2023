file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0
time_array = []
distance_array = []

# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    line_s = line_s.replace(" ", "")
    string_array = line_s.split(":")
    if string_array[0] == "Time":
        for i in range(1, len(string_array), 1):
            if string_array[i].isdigit():
                time_array.append(int(string_array[i]))
    if string_array[0] == "Distance":
        for i in range(1, len(string_array), 1):
            if string_array[i].isdigit():
                distance_array.append(int(string_array[i]))

print(time_array)
print(distance_array)

product_of_possible_values = 1
for i in range(len(time_array)):
    possible_values = 0
    distance = 0
    for time in range(time_array[i]+1):
        distance = time * (time_array[i] - time)
        if distance > distance_array[i]:
            possible_values += 1
    print("race {}, possible values: {}".format(i, possible_values))
    product_of_possible_values *= possible_values

print("final product of possible values = {}".format(product_of_possible_values))
