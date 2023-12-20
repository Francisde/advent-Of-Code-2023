file1 = open('input1.txt', 'r')
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
        return "{}{}{}:{}".format(self.variable, self.operator, self.value, self.destination)

    def condition_holds(self, check_value):
        if self.operator == "<":
            return check_value < self.value
        elif self.operator == ">":
            return check_value > self.value


class Rule:
    def __init__(self, name, conditions):
        self.name = name
        self.conditions = conditions


all_rules = []
all_parts = []
# Strips the newline character
parse_rules = True
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    if line_s == "":
        parse_rules = False
        continue
    if parse_rules:
        name = line_s.split("{")[0]
        rule_string = line_s.split("{")[1].replace("}", "")
        print(name)
        print(rule_string)
        conditions = []
        rule_strings = rule_string.split(",")
        for rule in rule_strings:
            if ":" not in rule:
                new_condition = Condition(None, None, None, rule, True)
                conditions.append(new_condition)
                continue
            variable = rule[0:1]
            condition = rule[1:2]
            print(variable)
            print(condition)
            value = int(rule[2:].split(":")[0])
            destination = rule[2:].split(":")[1]
            new_condition = Condition(variable, condition, value, destination)
            conditions.append(new_condition)
        new_rule = Rule(name, conditions)
        all_rules.append(new_rule)
    else:
        print("parse parts")
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
