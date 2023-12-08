import math

file1 = open('input3.txt', 'r')
Lines = file1.readlines()

count = 0

node_dict = dict()
start_nodes = []

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right

    def __str__(self):
        return "node: {}, ({}, {})".format(self.name, self.left.name, self.right.name)

    def __repr__(self):
        return str(self)

# parse insructions
instructions = Lines[0].strip()
print("Instructions: {}".format(instructions))
# parse nodes
for line in Lines[2::]:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    node_s = line_s.split(" = ")[0]
    print(node_s)
    node = Node(node_s, None, None)
    node_dict[node_s] = node
    if node_s.endswith("A"):
        start_nodes.append(node_s)

# parse childs
for line in Lines[2::]:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    node_s = line_s.split(" = ")[0]
    childs_s = line_s.split(" = ")[1]
    childs_s = childs_s.replace("(", "").replace(")", "").replace(",", "")
    childs_s = childs_s.split(" ")
    node_dict[node_s].add_left(node_dict[childs_s[0]])
    node_dict[node_s].add_right(node_dict[childs_s[1]])

print(node_dict)

# calc steps from AAA to ZZZ
steps = 0
current_nodes = []
print(start_nodes)
loop_steps = []
for node in start_nodes:
    current_nodes = [node_dict[node]]
    steps = 0

    while True:
        reached_zzz = False
        for character in instructions:
            next_step_nodes = []
            for current_node in current_nodes:
                if character == "L":
                    next_step_nodes.append(current_node.left)
                elif character == "R":
                    next_step_nodes.append(current_node.right)
            current_nodes = next_step_nodes
            steps += 1

            reached_zzz = True
            for current_node in current_nodes:
                if not current_node.name.endswith("Z"):
                    reached_zzz = False
            if reached_zzz:
                break
        if reached_zzz:
            loop_steps.append(steps)
            break

print(loop_steps)
print(math.lcm(18157, 11653, 21409, 12737, 14363, 15989))
print("total steps: {}".format(steps))

