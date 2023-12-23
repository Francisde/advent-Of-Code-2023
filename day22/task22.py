file1 = open('input1.txt', 'r')
Lines = file1.readlines()

count = 0

class Brick:
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def get_max_z(self):
        return max(self.coordinate1[2], self.coordinate2[2])

    def get_min_z(self):
        return min(self.coordinate1[2], self.coordinate2[2])

    def get_cubes_for_level_z(self, z):
        if z >= self.get_min_z() and z <= self.get_max_z():
            if self.get_min_z() == self.get_max_z():
                return [(self.coordinate1[0], self.coordinate1[1])]
            if self.coordinate1[0] != self.coordinate2[0]:
                result = []
                for i in range(min(self.coordinate1[0], self.coordinate2[0]), max(self.coordinate1[0], self.coordinate2[0] + 1)):
                    result.append((i, coordinates1[1]))
                return result
            if self.coordinate1[1] != self.coordinate2[1]:
                result = []
                for i in range(min(self.coordinate1[1], self.coordinate2[1]), max(self.coordinate1[1], self.coordinate2[1] + 1)):
                    result.append((coordinates1[0]), i)
                return result

class GameField:
    def __init__(self, bricks):
        self.bricks = bricks



initial_bricks = []
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    coordinates = line_s.split("~")
    coordinates1_s = coordinates[0].split(",")
    coordinates2_s = coordinates[1].split(",")
    coordinates1 = (int(coordinates1_s[0]), int(coordinates1_s[1]), int(coordinates1_s[2]))
    coordinates2 = (int(coordinates2_s[0]), int(coordinates2_s[1]), int(coordinates2_s[2]))
    initial_bricks.append(Brick(coordinates1, coordinates2))
