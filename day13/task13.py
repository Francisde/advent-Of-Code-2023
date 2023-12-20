file1 = open('input1.txt', 'r')
Lines = file1.readlines()

count = 0

class Pattern:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        result = ""
        for row in self.array:
            result = result + str(row) +"\n"
        return result +"\n"

    def __repr__(self):
        return str(self)

    def get_horizontal_reflection(self):
        print("horizontal")
        max_length = 0
        index = -1
        for i in range(len(self.array)):
            reverse_counter = i
            length = 0
            max_j = 0
            for j in range(i + 1, len(self.array), 1):
                if reverse_counter < 0:
                    reverse_counter = 0
                    break
                print("check {}vs{}".format(reverse_counter, j))
                if self.array[reverse_counter] == self.array[j]:
                    print(True)
                    length += 1
                    reverse_counter -= 1
                    max_j = j
                    print(max_j)
                else:
                    length = 0
                    break
            print("max_length {}".format(max_length))
            if length > max_length:
                if reverse_counter == 0 or max_j == len(self.array) -1 :
                    max_length = length
                    index = i
        return (index + 1, max_length)

    def get_vertical_reflection(self):
        print("vertical")
        max_length = 0
        index = -1
        for i in range(len(self.array[0])):
            reverse_counter = i
            length = 0
            max_j = 0
            for j in range(i + 1, len(self.array[0]), 1):
                if reverse_counter < 0:
                    reverse_counter = 0
                    break
                print("check {}vs{}".format(reverse_counter, j))
                match = True
                for row in self.array:
                    if row[reverse_counter] != row[j]:
                        match = False
                if match:
                    print(True)
                    length += 1
                    reverse_counter -= 1
                    max_j = j
                else:
                    length = 0
                    break
            if length > max_length:
                if reverse_counter == 0 or max_j == len(self.array[0]) -1:
                    max_length = length
                    index = i
        return (index + 1, max_length)





array = []
patterns = []
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    if len(line_s) == 0:
        patterns.append(Pattern(array))
        array = []
    else:
        row = [x for x in line_s]
        array.append(row)
result = 0
for i in range(len(patterns)):
    print("Pattern {}".format(i))
    print(patterns[i])
    horizontal_index = patterns[i].get_horizontal_reflection()
    vertical_index = patterns[i].get_vertical_reflection()
    print("horizontal index = {}, length: {}".format(horizontal_index[0], horizontal_index[1]))
    print("vertical index = {}, length: {}".format(vertical_index[0], vertical_index[1]))
    if vertical_index[1] > horizontal_index[1]:
        result += vertical_index[0]
    elif vertical_index[1] < horizontal_index[1]:
        result += (horizontal_index[0] * 100)
    else:
        print("DANGER!!!")
    v_len = len(patterns[i].array[0])
    h_len = len(patterns[i].array)
    a = (vertical_index[0] - vertical_index[1] == 0 or vertical_index[0] + vertical_index[1] == v_len) and vertical_index[1] > 0
    b = (horizontal_index[0] - horizontal_index[1] == 0 or horizontal_index[0] + horizontal_index[1] == h_len) and horizontal_index[1] > 0
    print("{}-{}".format(a, b))

print("Final result: {}".format(result))
