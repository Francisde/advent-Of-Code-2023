import itertools
from multiprocessing import Pool
import time

file_count = 12

file1 = open("input{}.txt".format(file_count), 'r')
Lines = file1.readlines()

count = 0

class Game:
    def __init__(self, row, groups, arrangement=0):
        self.row = row
        self.groups = groups
        self.arrangement = arrangement

    def __str__(self):
        return self.row + " : " + str(self.groups)

    def __repr__(self):
        return str(self)

    def get_permutation_string(self):
        count_unknown = self.row.count("?")
        count_damaged_known = self.row.count("#")
        count_damaged_total = 0
        for group in self.groups:
            count_damaged_total += group
        result = ""
        for i in range(count_unknown):
            if count_damaged_total > count_damaged_known:
                result += "#"
                count_damaged_total -=1
            else:
                result += "."
        return result
    def arrangement_fits(self, arrangement):
        for i in range(len(self.row)):
            if self.row[i] == "#" and arrangement[i] != "#":

                return False
            if self.row[i] == "." and arrangement[i] != ".":

                return False
        arrangement_groups = []
        dammaged_count = 0
        current_run = False
        for i in range(len(arrangement)):
            if arrangement[i] == "#" and current_run is False:
                dammaged_count = 1
                current_run = True
                if i == len(arrangement) -1:
                    arrangement_groups.append(dammaged_count)
                    dammaged_count = 0
            elif arrangement[i] == "#" and current_run is True:
                dammaged_count += 1
                if i == len(arrangement) -1:
                    arrangement_groups.append(dammaged_count)
                    dammaged_count = 0
            elif arrangement[i] == "." and current_run is True:
                current_run = False
                arrangement_groups.append(dammaged_count)
                dammaged_count = 0

        if arrangement_groups == self.groups:

            return True
        return False


def clean_up(arrangements):
    result = []
    for arrangement in arrangements:
        if arrangement in result:
            pass
        else:
            result.append(arrangement)
    return result


def generate_permutations(count_x, count_y):
    #print("count_x: {}, count_y: {}".format(count_x, count_y))
    result = []
    # case x
    if count_x > 0:
        suffixes = generate_permutations(count_x - 1, count_y)
        for value in suffixes:
            #print("values {}".format(value))
            res = ["#"]
            res = res + value
            result.append(res)
    # case x
    if count_y > 0:
        suffixes = generate_permutations(count_x , count_y - 1)
        for value in suffixes:
            res = ["."]
            res = res + value
            result.append(res)
    if count_y == 0 and count_x == 0:
        return [[]]
    return result

game_rows = []
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    split_string = line_s.split(" ")
    groups_s = split_string[1].split(",")
    groups = [int(x) for x in groups_s]
    game_rows.append(Game(split_string[0], groups))

print(game_rows)
arrangement_sum = 0
def get_arragements(row):

    # get all arangements
    permutation_s = row.get_permutation_string()
    count_1 = permutation_s.count("#")
    count_2 = permutation_s.count(".")

    #all_arangements = set(itertools.permutations(permutation_s, len(permutation_s)))
    all_arangements = generate_permutations(count_1, count_2)
    all_arangements = clean_up(all_arangements)
    arrangement_count = 0
    print("permutation_s: {} count1 {}, count2 {}, arangements: {}".format(permutation_s, count_1, count_2, len(all_arangements)))

    for arrangement in all_arangements:

        teststring = row.row
        for character in arrangement:
            teststring = teststring.replace("?", character, 1)

        if row.arrangement_fits(teststring):
            arrangement_count += 1
    # test if it fits
    print("row: {}, arrangements: {}".format(row, arrangement_count))
    return arrangement_count

def demo_multi_processing():
    tic = time.time()
    pool = Pool(processes=32)
    res = list(pool.apply_async(get_arragements, args=(name,)) for name in game_rows)

    pool.close()
    pool.join()

    results = [r.get() for r in res]
    print(results)
    arrangement_sum = 0
    for i in results:
        arrangement_sum += i
    print("arrangement_sum: {}".format(arrangement_sum))
    file2 = open("output{}.txt".format(file_count), 'w')
    file2.write("arrangement_sum: {}".format(arrangement_sum))
    toc = time.time()
    print(f'Completed in {toc - tic} seconds')

if __name__ == '__main__':
    demo_multi_processing()

print("test")
print(generate_permutations(2,3))