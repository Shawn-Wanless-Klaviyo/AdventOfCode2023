def part1(input_file):
    score = 0
    for line in input_file.readlines():
        card_id, card = line.strip().split(":")
        winning_pool, player_pool = card.split("|")
        winning_pool = set(num.strip() for num in winning_pool.split(" ") if len(num.strip()) > 0)
        player_pool = set(num.strip() for num in player_pool.split(" ") if len(num.strip()) > 0)
        winning_nums = player_pool.intersection(winning_pool)
        if len(winning_nums) > 0:
            score += 2 ** (len(winning_nums) - 1)
    return score


def part2(input_file):
    card_matches = {}
    lines = input_file.readlines()
    for line in lines:
        card_id, card = line.strip().split(":")
        winning_pool, player_pool = card.split("|")
        winning_pool = set(num.strip() for num in winning_pool.split(" ") if len(num.strip()) > 0)
        player_pool = set(num.strip() for num in player_pool.split(" ") if len(num.strip()) > 0)
        winning_nums = player_pool.intersection(winning_pool)
        if len(winning_nums) > 0:
            card_num = int(card_id.split(" ")[-1])
            card_matches[card_num] = len(winning_nums)
    card_instances = [1 for _ in lines]
    _process_card_copies(card_instances, card_matches)
    return sum(card_instances)


def _process_card_copies(card_instances, card_matches):
    for card_index, card_count in enumerate(card_instances):
        match_count = card_matches.get(card_index + 1, 0)
        for i in range(match_count):
            card_instances[card_index + 1 + i] += card_count
