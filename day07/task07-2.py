import itertools

file1 = open('input2.txt', 'r')
Lines = file1.readlines()

count = 0

card_list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

cards = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12
}

game_types = {
    "Five of a kind": 6,
    "Four of a kind": 5,
    "Full house": 4,
    "Three of a kind": 3,
    "Two pair": 2,
    "One pair": 1,
    "High card": 0
}

def get_all_combinations(size):
    results = []
    for comb in itertools.product(card_list, repeat=size):
        results.append(comb)
    return results


class Hand:

    def __init__(self, hand: str, bid: int, game_type=None, rank=None):
        self.hand = hand
        self.bid = bid
        self.game_type = game_type
        self.rank = rank

    def __lt__(self, other):
        if game_types[self.getGameType()] < game_types[other.getGameType()]:
            return True
        elif game_types[self.getGameType()] == game_types[other.getGameType()]:
            for i in range(len(self.hand)):
                if cards[self.hand[i]] < cards[other.hand[i]]:
                    return True
                elif cards[self.hand[i]] == cards[other.hand[i]]:
                    pass
                else:
                    return False
        else:
            return False

    def __gt__(self, other):
        return not self < other

    def __str__(self):
        return "hand: {}, bid: {}, rank: {}".format(self.hand, self.bid, self.rank)

    def __repr__(self):
        return str(self)



    def getGameType(self):
        if self.game_type is None:
            if self.has_joker():
                self.game_type = self.get_best_game_type()
            elif self.is_five_of_a_kind():
                self.game_type = "Five of a kind"
            elif self.is_four_of_a_kind():
                self.game_type = "Four of a kind"
            elif self.is_full_house():
                self.game_type = "Full house"
            elif self.is_three_of_a_kind():
                self.game_type = "Three of a kind"
            elif self.is_two_pair():
                self.game_type = "Two pair"
            elif self.is_one_pair():
                self.game_type = "One pair"
            else:
                self.game_type = "High card"
        return self.game_type

    def has_joker(self):
        for card in self.hand:
            if card == "J":
                return True
        return False

    def get_best_game_type(self):
        best_game_type = "High card"
        number_of_joker = self.hand.count("J")
        combinations = get_all_combinations(number_of_joker)
        for comb in combinations:
            temp_hand_str = self.hand
            for character in comb:
                temp_hand_str = temp_hand_str.replace("J", character, 1)
            temp_hand = Hand(temp_hand_str, 0)
            if game_types[best_game_type] < game_types[temp_hand.getGameType()]:
                best_game_type = temp_hand.getGameType()
        return best_game_type

    def is_five_of_a_kind(self):
        result_set = set()
        for card in self.hand:
            result_set.add(card)
        if len(result_set) == 1:
            return True
        else:
            return False

    def is_four_of_a_kind(self):
        result_set = set()
        for card in self.hand:
            result_set.add(card)
        if len(result_set) == 2:
            for set_card in result_set:
                if self.hand.count(set_card) == 4:
                    return True
        return False

    def is_three_of_a_kind(self):
        result_set = set()
        for card in self.hand:
            result_set.add(card)
        if len(result_set) == 3:
            for set_card in result_set:
                if self.hand.count(set_card) == 3:
                    return True
        return False

    def is_full_house(self):
        result_set = set()
        for card in self.hand:
            result_set.add(card)
        if len(result_set) == 2:
            if not self.is_four_of_a_kind():
                return True
        return False

    def is_two_pair(self):
        result_set = set()
        for card in self.hand:
            result_set.add(card)
        if len(result_set) == 3:
            if not self.is_three_of_a_kind():
                return True
        return False

    def is_one_pair(self):
        result_set = set()
        for card in self.hand:
            result_set.add(card)
        if len(result_set) == 4:
            return True
        return False

    def is_high_card(self):
        result_set = set()
        for card in self.hand:
            result_set.add(card)
        if len(result_set) == 5:
            return True
        return False

    def calc_wining(self):
        if self.rank is None:
            return 0
        else:
            return self.rank * self.bid

# Strips the newline character
list_of_cards = []
for line in Lines:
    line_s = line.strip()
    count += 1
    print("Line {}, text:{}".format(count, line_s))
    split_line = line_s.split(" ")
    list_of_cards.append(Hand(split_line[0], int(split_line[1])))

print(list_of_cards)
list_of_cards.sort()
print(list_of_cards)

for i in range(len(list_of_cards)):
    list_of_cards[i].rank = i+1
print(list_of_cards)


# calc the total winning
total_winnings = 0
for hand in list_of_cards:
    total_winnings += hand.calc_wining()
print("Total winnings: {}".format(total_winnings))
