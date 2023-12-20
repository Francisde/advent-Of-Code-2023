file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0


class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.state = "in"

    def __str__(self):
        return "x={},m={},a={},s={}, state= {}".format(self.x, self.m, self.a, self.s, self.state)

    def __repr__(self):
        return str(self)


class Condition:
    def __init__(self, variable, operator, value, destination, default=False):
        self.variable = variable
        self.operator = operator
        self.value = value
        self.destination = destination
        self.default = default

    def __str__(self):
        if self.default:
            return "default-{}".format(self.destination)
        #return "{}{}{}:{}".format(self.variable, self.operator, self.value, self.destination)
        return "{}{}{}".format(self.variable, self.operator, self.value)

    def condition_holds(self, check_value):
        if self.operator == "<":
            return check_value < self.value
        elif self.operator == ">":
            return check_value > self.value

    def get_negation(self):
        if self.default:
            return "PROBLEM!"
        if self.operator == "<":
            return "{}>{}".format(self.variable, self.value - 1)
        if self.operator == ">":
            return "{}<{}".format(self.variable, self.value + 1)


class Rule:
    def __init__(self, name, conditions):
        self.name = name
        self.conditions = conditions

    def __str__(self):
        return self.name


all_rules = []
all_parts = []
# Strips the newline character
parse_rules = True
for line in Lines:
    line_s = line.strip()
    count += 1
    # print("Line {}, text:{}".format(count, line_s))
    if line_s == "":
        parse_rules = False
        continue
    if parse_rules:
        name = line_s.split("{")[0]
        rule_string = line_s.split("{")[1].replace("}", "")
        # print(name)
        # print(rule_string)
        conditions = []
        rule_strings = rule_string.split(",")
        for rule in rule_strings:
            if ":" not in rule:
                new_condition = Condition(None, None, None, rule, True)
                conditions.append(new_condition)
                continue
            variable = rule[0:1]
            condition = rule[1:2]
            # print(variable)
            # print(condition)
            value = int(rule[2:].split(":")[0])
            destination = rule[2:].split(":")[1]
            new_condition = Condition(variable, condition, value, destination)
            conditions.append(new_condition)
        new_rule = Rule(name, conditions)
        all_rules.append(new_rule)
    else:
        # print("parse parts")
        line_s = line_s.replace("{", "").replace("}", "")
        values = line_s.split(",")
        x = int(values[0].split("=")[1])
        m = int(values[1].split("=")[1])
        a = int(values[2].split("=")[1])
        s = int(values[3].split("=")[1])
        part = Part(x, m, a, s)
        all_parts.append(part)

for part in all_parts:
    while True:
        if part.state == "A" or part.state == "R":
            break
        for rule in all_rules:
            if rule.name == part.state:
                for condition in rule.conditions:
                    if condition.default:
                        part.state = condition.destination
                        break
                    elif condition.variable == "x":
                        if condition.condition_holds(part.x):
                            part.state = condition.destination
                            break
                    elif condition.variable == "m":
                        if condition.condition_holds(part.m):
                            part.state = condition.destination
                            break
                    elif condition.variable == "a":
                        if condition.condition_holds(part.a):
                            part.state = condition.destination
                            break
                    elif condition.variable == "s":
                        if condition.condition_holds(part.s):
                            part.state = condition.destination
                            break
                    else:
                        print("ERROR")


solution = 0
for part in all_parts:
    if part.state == "A":
        solution += part.x
        solution += part.m
        solution += part.a
        solution += part.s
print(solution)


# generate all conditions to A
in_rule = None
for rule in all_rules:
    if rule.name == "in":
        in_rule = rule
        break

condition_chains = []

def generate_condition(input_string, rule):
    #print("generate conditions: {}".format(rule) )
    for condition in rule.conditions:
        if condition.destination == "A":
            output = ""
            if not condition.default:
                output =input_string + " , " + str(condition)
            else:
                output =input_string
            print(output)
            condition_chains.append(output)
        elif condition.destination == "R":
            #print(input_string + ", " + str(condition))
            pass
        else:
            if not condition.default:
                output_string = input_string + " , " + str(condition)
            else:
                output_string = input_string

            output_rule = None
            for rule in all_rules:
                if rule.name == condition.destination:
                    output_rule = rule
                    break
            generate_condition(output_string, output_rule)
        input_string = input_string + " , " + condition.get_negation()

generate_condition("in", in_rule)
all_possible_combinations = 0
print(len(condition_chains))
for condition_chain in condition_chains:
    possible_x = [x for x in range(1, 4001)]
    possible_m = [x for x in range(1, 4001)]
    possible_a = [x for x in range(1, 4001)]
    possible_s = [x for x in range(1, 4001)]
    conditions = condition_chain.split(" , ")[1:]
    for inner_condition in conditions:
        variable = inner_condition[0:1]
        operator = inner_condition[1:2]
        value = int(inner_condition[2:])
        if variable == "x":
            if operator == "<":
                filteredObject = filter(lambda k: k < value, possible_x)
            else:
                filteredObject = filter(lambda k: k > value, possible_x)
            possible_x = list(filteredObject)
        if variable == "m":
            if operator == "<":
                filteredObject = filter(lambda k: k < value, possible_m)
            else:
                filteredObject = filter(lambda k: k > value, possible_m)
            possible_m = list(filteredObject)
        if variable == "a":
            if operator == "<":
                filteredObject = filter(lambda k: k < value, possible_a)
            else:
                filteredObject = filter(lambda k: k > value, possible_a)
            possible_a = list(filteredObject)
        if variable == "s":
            if operator == "<":
                filteredObject = filter(lambda k: k < value, possible_s)
            else:
                filteredObject = filter(lambda k: k > value, possible_s)
            possible_s = list(filteredObject)

    possible_combinations = len(possible_x) * len(possible_m) * len(possible_a) * len(possible_s)
    print(possible_combinations)
    all_possible_combinations += possible_combinations

print(all_possible_combinations)