def part1(input_file):
    color_counts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    possible_id_sum = 0
    for line in input_file.readlines():
        possible = True
        game_tag, game = line.strip().split(":")
        game_id = int(game_tag.split(" ")[-1])
        game_rounds = game.strip().split("; ")
        for game_round in game_rounds:
            cubes = game_round.strip().split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                if int(count) > color_counts[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_id_sum += game_id
    return possible_id_sum


def part2(input_file):
    power_set_sum = 0
    for line in input_file.readlines():
        max_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        _, game = line.strip().split(":")
        game_rounds = game.strip().split("; ")
        for game_round in game_rounds:
            cubes = game_round.strip().split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                if int(count) > max_colors[color]:
                    max_colors[color] = int(count)
        power_set = max_colors["red"] * max_colors["green"] * max_colors["blue"]
        power_set_sum += power_set
    return power_set_sum
