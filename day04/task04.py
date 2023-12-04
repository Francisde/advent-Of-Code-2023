file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0
sum = 0
winning_sum = 0

class CardPile:
    def __init__(self, number, copies):
        self.number = number
        self.copies = copies

    def add_copie(self, factor):
        self.copies += factor


card_list = []
# Strips the newline character
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    card_list.append(CardPile(count, 0))

print(len(card_list))
count = 0
for line in Lines:
    line_s = line.strip()
    line_s = line_s.replace("  ", " ")
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    line_s = line_s.split(":")[1].strip()
    piles = line_s.split(" | ")
    winning_numbers = [int(x) for x in piles[0].split(" ")]

    my_numbers = [int(x) for x in piles[1].split(" ")]
    card_index = count - 1
    multiply_factor = card_list[card_index].copies + 1
    card_index += 1
    win = 0
    for x in winning_numbers:
        for num in my_numbers:
            if x == num:
                print("card_index: {}".format(card_index))
                card_list[card_index].add_copie(multiply_factor)
                card_index += 1
                if win == 0:
                    win = 1
                else:
                    win = win * 2
    winning_sum += win

print(winning_sum)

# count all cards
card_sum = 0
for card in card_list:
    card_sum += (1 + card.copies)

print("card_sum: {}".format(card_sum))