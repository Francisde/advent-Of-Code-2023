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

permutation_cache = dict()
def generate_permutations(count_x, count_y):
    #print("count_x: {}, count_y: {}".format(count_x, count_y))
    result = []
    key = "{}-{}".format(count_x, count_y)
    if key in permutation_cache:
        return permutation_cache[key]
    # case x
    if count_x > 0:
        suffixes = generate_permutations(count_x - 1, count_y)
        for value in suffixes:
            #print("values {}".format(value))
            res = "#"
            res = res + value
            result.append(res)
    # case x
    if count_y > 0:
        suffixes = generate_permutations(count_x , count_y - 1)
        for value in suffixes:
            res = "."
            res = res + value
            result.append(res)
    if count_y == 0 and count_x == 0:
        return [""]
    permutation_cache[key] = result
    return result


hit_count = 0
current_game = None

def generate_permutations_forward(count_x, count_y, substring = ""):
    # case x
    if count_x > 0:
        new_substring = substring + "x"
        generate_permutations_forward(count_x - 1, count_y, new_substring)

    # case x
    if count_y > 0:
        new_substring = substring + "."
        suffixes = generate_permutations_forward(count_x , count_y - 1, new_substring)

    if count_y == 0 and count_x == 0:
        if current_game.arrangement_fits(substring):
            global.hit_count += 1


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
def get_arragements(row, arrangement):

    teststring = row.row
    for character in arrangement:
        teststring = teststring.replace("?", character, 1)

    if row.arrangement_fits(teststring):
        return 1
    # test if it fits
    return 0

def get_all_arangements(row):
    # get all arangements
    permutation_s = row.get_permutation_string()
    count_1 = permutation_s.count("#")
    count_2 = permutation_s.count(".")

    #all_arangements = set(itertools.permutations(permutation_s, len(permutation_s)))
    all_arangements = generate_permutations(count_1, count_2)
    print("ready all arangement {}".format(len(all_arangements)))
    print("cache_size: {}".format(len(permutation_cache.keys())))
    #all_arangements = clean_up(all_arangements)
    return all_arangements

def demo_multi_processing():
    tic = time.time()
    pool = Pool(processes=1)
    arrangement_sum = 0
    for game in game_rows:
        all_arrangements = get_all_arangements(game)
        res = list(pool.apply_async(get_arragements, args=(game, arrangement)) for arrangement in all_arrangements)
        results = [r.get() for r in res]
        local_arragement_sum = 0
        for i in results:
            local_arragement_sum += i
        print("game: {} arragement_sum = {}".format(game, local_arragement_sum))
        print(len(permutation_cache.keys()))
        arrangement_sum += local_arragement_sum
    pool.close()
    pool.join()


    print("arrangement_sum: {}".format(arrangement_sum))
    file2 = open("output{}.txt".format(file_count), 'w')
    file2.write("arrangement_sum: {}".format(arrangement_sum))
    toc = time.time()
    print(f'Completed in {toc - tic} seconds')

if __name__ == '__main__':
    demo_multi_processing()
