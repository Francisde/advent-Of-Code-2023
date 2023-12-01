file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0
sum = 0

string_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    first_digit = ""
    first_digit_index = len(line_s)
    second_digit = ""
    second_digit_index = 0

    for character in line_s:
        if character.isdigit():
            first_digit = character
            first_digit_index = line_s.find(first_digit)
            break
    for character in line_s[::-1]:
        if character.isdigit():
            second_digit = character
            second_digit_index = line_s.rfind(second_digit)
            break
    for count in range(len(string_numbers)):
        l_index = line_s.find(string_numbers[count])
        r_index = line_s.rfind(string_numbers[count])
        if l_index < first_digit_index and l_index != -1:
            first_digit_index = l_index
            first_digit = "{}".format(count+1)
        if r_index > second_digit_index and r_index != -1:
            second_digit_index = r_index
            second_digit = "{}".format(count+1)


    number = first_digit + second_digit
    number = int(number)
    print("1: {}, 2: {}".format(first_digit_index, second_digit_index))
    print(number)
    sum += number
print("Result: {}".format(sum))


