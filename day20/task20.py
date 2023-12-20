from time import sleep

file1 = open('input3.txt', 'r')
Lines = file1.readlines()

count = 0


class Modul:
    def __init__(self, name, module_type, outputs_string):
        self.name = name
        self.module_type = module_type
        self.outputs_string = outputs_string
        self.output_module = []
        self.input_module = []
        self.conjunction_input = []
        self.output_pulse = "HIGH"
        self.input_pulse = "HIGH"
        self.flip_flop = "OFF"

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def init_conjunction(self):
        if self.module_type != "&":
            return
        else:
            self.conjunction_input = []
            for i in self.input_module:
                print("init: {}".format(i.name))
                self.conjunction_input.append("LOW")

    def set_input_module(self, input_modul):
        self.input_module.append(input_modul)

    def react(self, signal):
        result = []
        if self.name == "broadcaster":
            self.output_pulse = self.input_pulse
            for module in self.output_module:
                module.input_pulse = self.output_pulse
            for node in self.output_module:
                result.append((node, self.output_pulse, self))

        elif self.module_type == "%":
            #print("flip-flop mode: {}".format(self.flip_flop))

            if self.input_pulse == "HIGH":
                return []
            if self.input_pulse == "LOW" and self.flip_flop == "OFF":
                self.flip_flop = "ON"
                self.output_pulse = "HIGH"
            elif self.input_pulse == "LOW" and self.flip_flop == "ON":
                self.flip_flop = "OFF"
                self.output_pulse = "LOW"
            for module in self.output_module:
                module.input_pulse = self.output_pulse
            for node in self.output_module:
                result.append((node, self.output_pulse, self))
        elif self.module_type == "&":
            all_high = True
            index_to_change = self.input_module.index(signal[2])
            self.conjunction_input[index_to_change] = signal[1]
            for i in self.conjunction_input:
                if i == "LOW":
                    all_high =False
            if all_high:
                self.output_pulse ="LOW"
            else:
                self.output_pulse ="HIGH"
            for module in self.output_module:
                module.input_pulse = self.output_pulse
            for node in self.output_module:
                result.append((node, self.output_pulse, self))


        else:
            print("ERROR not defined + "+self.name)
            return []
        return result



all_output_strings = []
modules = []
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    module_s = line_s.split(" -> ")[0]
    if "broadcaster" in module_s:
        pass
        module_name = "broadcaster"
        module_type = "broadcaster"
        output_strings = line_s.split(" -> ")[1]
        output_strings = output_strings.split(", ")
        modules.append(Modul(module_name, module_type, output_strings))
    else:
        module_type = module_s[0:1]
        module_name = module_s[1:]
        output_strings = line_s.split(" -> ")[1]
        output_strings = output_strings.split(", ")
        modules.append(Modul(module_name, module_type, output_strings))
        for string_ in output_strings:
            all_output_strings.append(string_)


print(len(all_output_strings))
for output_string in all_output_strings:
    print(output_string)
    in_list = False
    for module in modules:
        if module.name == output_string:
            print(module.name)
            in_list = True
    if not in_list:
        print("ACHTUNG: {} not in modules".format(output_string))
        modules.append(Modul(output_string, "%", []))

print(modules)

# parse output_nodes and input_nodes
for module in modules:
    for node_s in module.outputs_string:
        for inner_module in modules:
            if inner_module.name == node_s:
                module.output_module.append(inner_module)
                inner_module.input_module.append(module)


broadcast_module = None
for module in modules:
    if module.name == "broadcaster":
        broadcast_module = module
    else:
        module.init_conjunction()

queue = []
low_counter = 0
high_counter = 0


button_counter = 0
diff_rr = 0
diff_bs = 0
diff_zb = 0
diff_js = 0
while button_counter < 100000:
    button_counter += 1
    queue.append((broadcast_module, "LOW", "button"))
    low_counter += 1

    while len(queue) > 0:
        current_signal = queue.pop(0)
        #print(current_signal)
        current_signal[0].input_pulse = current_signal[1]
        #print("start node {}, input {}, old output {}".format(current_signal[0].name, current_signal[0].input_pulse, current_signal[0].output_pulse))
        next_nodes = current_signal[0].react(current_signal)
        #sleep(1)
        #print("processed node {}, output {}".format(current_signal[0].name, current_signal[0].output_pulse))
        #print(next_nodes)
        #print()
        for i in next_nodes:
            queue.append(i)
            if i[1] == "LOW":
                low_counter += 1
                if i[0].name == "rx":
                    print("Reached rx with low")
                    sleep(10)
            else:
                if i[2].name == "js" and diff_js == 0:
                    print("js send high after {} button presses, diff: {}".format(button_counter, button_counter - 0))
                    diff_js = button_counter - 0
                if i[2].name == "zb" and diff_zb == 0:
                    print("zb send high after {} button presses, diff: {}".format(button_counter, button_counter - 0))
                    diff_zb = button_counter - 0
                if i[2].name == "bs" and diff_bs == 0:
                    print("bs send high after {} button presses, diff: {}".format(button_counter, button_counter - 0))
                    diff_bs = button_counter - 0
                if i[2].name == "rr" and diff_rr == 0:
                    print("rr send high after {} button presses, diff: {}".format(button_counter, button_counter - 0))
                    diff_rr = button_counter - 0
                high_counter += 1

print("Low counter: {}".format(low_counter))
print("High counter: {}".format(high_counter))

print("Final result: {}".format(low_counter * high_counter))
diff_rr = 3733
diff_bs = 4001
diff_zb = 4021
diff_js = 3761
print(diff_rr * diff_bs * diff_zb * diff_js)