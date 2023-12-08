from functools import total_ordering
from enum import IntEnum
from collections import defaultdict

PART2 = False


@total_ordering
class Hand:
    class HandType(IntEnum):
        HIGH_CARD = 1
        ONE_PAIR = 2
        TWO_PAIR = 3
        THREE_OF_KIND = 4
        FULL_HOUSE = 5
        FOUR_OF_KIND = 6
        FIVE_OF_KIND = 7

    card_weights = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        **{str(num): num for num in range(2, 10)}
    }

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.part2 = PART2
        if self.part2:
            self.card_weights["J"] = 1
        self.type = self._determine_type(cards)

    def __lt__(self, other):
        for self_char, other_char in zip(self.cards, other.cards):
            if self_char != other_char:
                return self.card_weights[self_char] < self.card_weights[other_char]
        return False

    def __eq__(self, other):
        return self.cards == other.cards

    def _determine_type(self, cards):
        mapping = defaultdict(int)
        max_count = 0
        for card in cards:
            mapping[card] += 1
            if mapping[card] > max_count:
                max_count = mapping[card]

        # handle jokers for part2
        jack_card = "J"
        if self.part2 and jack_card in mapping and len(mapping) != 1:
            mapping_sorted_by_count = sorted(mapping.items(), key=lambda x: x[1])
            most_common_card, most_common_count = mapping_sorted_by_count[-1]
            if most_common_card == jack_card:
                next_most_common_card, next_most_common_count = mapping_sorted_by_count[-2]
                mapping[next_most_common_card] = next_most_common_count + most_common_count
                max_count = mapping[next_most_common_card]
            else:
                mapping[most_common_card] = most_common_count + mapping[jack_card]
                max_count = mapping[most_common_card]
            del mapping[jack_card]

        if max_count == 5:
            return self.HandType.FIVE_OF_KIND
        if max_count == 4:
            return self.HandType.FOUR_OF_KIND
        if max_count == 3:
            if len(mapping) == 2:
                return self.HandType.FULL_HOUSE
            return self.HandType.THREE_OF_KIND
        if max_count == 2:
            if len(mapping) == 3:
                return self.HandType.TWO_PAIR
            return self.HandType.ONE_PAIR
        return self.HandType.HIGH_CARD


def part1(input_file):
    hand_type_buckets = defaultdict(list)
    for line in input_file.readlines():
        cards, bid = line.strip().split(" ")
        hand = Hand(cards, int(bid))
        hand_type_buckets[hand.type].append(hand)

    hand_type_buckets = [sorted(hand_type_buckets[key]) for key in sorted(hand_type_buckets.keys())]
    total_winnings = 0
    rank = 1
    for bucket in hand_type_buckets:
        for hand in bucket:
            total_winnings += hand.bid * rank
            rank += 1
    return total_winnings


def part2(input_file):
    global PART2
    PART2 = True
    return part1(input_file)
