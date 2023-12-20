Lines = []
file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0

class Lense:
    def __init__(self, label, value):
        self.label = label
        self.value = value

    def __str__(self):
        return "[{} {}]".format(self.label, self.value)

    def __repr__(self):
        return str(self)


class Box():
    def __init__(self, number):
        self.number = number
        self.lenses = []

    def add_lens(self, lense):
        # check if we should update
        for lens in self.lenses:
            if lens.label == lense.label:
                lens.value = lense.value
                return
        self.lenses.append(lense)

    def remove_lens(self, label):
        for lens in self.lenses:
            if lens.label == label:
                self.lenses.remove(lens)
                return

    def get_focus_power(self):
        focus_power = 0
        for i in range(len(self.lenses)):
            lense_power = (self.number + 1) * (i + 1) * self.lenses[i].value
            focus_power += lense_power
        return focus_power

def get_hash(input_string):
    current_value = 0
    for character in input_string:
        current_value += ord(character)
        current_value *= 17
        current_value = current_value % 256
    return current_value

boxes = dict()
for i in range(256):
    boxes[i] = Box(i)


# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    list_of_values = line_s.split(",")
    hash_sum = 0
    for value in list_of_values:
        if value.count("=") == 1:
            value_array = value.split("=")
            box_number = get_hash(value_array[0])
            boxes[box_number].add_lens(Lense(value_array[0], int(value_array[1])))
        else:
            value_array = value.split("-")
            box_number = get_hash(value_array[0])
            boxes[box_number].remove_lens(value_array[0])

total_focus_power = 0
for i in range(256):

    total_focus_power += boxes[i].get_focus_power()

print(total_focus_power)
print(get_hash("cm"))