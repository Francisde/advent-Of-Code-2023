file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0
sum = 0


class Cubes:

    def __init__(self, id, red, blue, green):
        self.id = id
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return "id: {}, red: {}, blue: {}, green: {}".format(self.id, self.red, self.blue, self.green)

    def fit_configuration(self, reds, blues, greens):
        if self.red <= reds and self.blue <= blues and self.green <= greens:
            return True
        return False

    def cube_power(self):
        return self.red * self.green * self.blue

def parse_cubes(input):
    # parse id
    id_string = input.split(":")[0]
    id = int(id_string.split(" ")[1])

    # split runs
    input = input.split(":")[1]
    runs = input.split(";")
    max_red = 0
    max_green = 0
    max_blue = 0

    for run in runs:
        # split colors
        colors = run.split(",")
        for color in colors:
            color_array = color.strip().split(" ")
            color_count = int(color_array[0])
            if color_array[1] == "red":
                if color_count > max_red:
                    max_red = color_count
            elif color_array[1] == "blue":
                if color_count > max_blue:
                    max_blue = color_count
            elif color_array[1] == "green":
                if color_count > max_green:
                    max_green = color_count
    return Cubes(id, max_red, max_blue, max_green)

cube_configurations = []
result = 0
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    cube_configurations.append(parse_cubes(line_s))

power_sum = 0
for cube in cube_configurations:
    print(cube)
    power_sum += cube.cube_power()
    print("id: {}, Power: {}".format(cube.id, cube.cube_power()))
    if cube.fit_configuration(12, 14, 13):
        result += cube.id

print("result: {}".format(result))
print("power: {}".format(power_sum))
