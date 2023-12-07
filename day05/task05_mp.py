from multiprocessing import Pool
import os
import time

file1 = open('input1.txt', 'r')
Lines = file1.readlines()

Lines.append("\n")
count = 0
sum = 0


def get_local_minimum(borders):
    parse = False
    parsed = False
    last_mapping = False
    minimum_location = -1

    for j in range(borders[1]):

        seed = borders[0]+j
        for line in Lines:
            line_s = line.strip()

            if line_s.endswith("map:"):
                parse = True
                parsed = False

                if line_s.startswith("humidity-to-location"):
                    last_mapping = True
                continue
            if len(line_s) == 0:
                parse = False
                if last_mapping:
                    #location_array.append(seed)
                    if minimum_location == -1:
                        minimum_location = seed
                    elif minimum_location > seed:
                        minimum_location = seed
                    last_mapping = False
                # TODO if parsed == False
            if parse and not parsed:
                old_seed = seed
                mapping = [int(x) for x in line_s.split(" ")]
                if mapping[1] <= seed < mapping[1] + mapping[2]:
                    diff = seed - mapping[1]
                    seed = mapping[0] + diff
                    parsed = True
    return minimum_location


# parse seeds:
seed_array = []
seed_pairs = [int(x) for x in Lines[0].strip().split(" ")[1::]]
print(seed_array)
# Strips the newline character
parse = False
parsed = False
last_mapping = False
minimum_location = -1
print("start parsing {} seeds".format(len(seed_array)))
input_pairs = []
for i in range(0, len(seed_pairs), 2):
    print("parse seed {}".format(i))
    input = (seed_pairs[i], seed_pairs[i+1])
    input_pairs.append(input)



def demo_multi_processing():
    tic = time.time()
    pool = Pool(processes=2)
    res = list(pool.apply_async(get_local_minimum, args=(name,)) for name in input_pairs)

    pool.close()
    pool.join()

    results = [r.get() for r in res]
    print(results)
    results.sort()
    print(results)
    print("min location: {}".format(results[0]))
    file2 = open('output2.txt', 'w')
    file2.write("min location: {}".format(results[0]))
    toc = time.time()
    print(f'Completed in {toc - tic} seconds')

if __name__ == '__main__':
    demo_multi_processing()