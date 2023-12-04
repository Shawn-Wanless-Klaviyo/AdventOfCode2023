def part1(input_file):
    engine_part_sum = 0
    schematic = [line.strip() for line in input_file.readlines()]
    for row in range(len(schematic)):
        curr_num = ""
        is_engine_part = False
        for col in range(len(schematic[row])):
            char = schematic[row][col]
            if char.isnumeric():
                curr_num += char
                if not is_engine_part and _neighbors_symbol(schematic, row, col):
                    is_engine_part = True
                if is_engine_part and not _safe_index(schematic, row, col + 1).isnumeric():
                    engine_part_sum += int(curr_num)
            else:
                curr_num = ""
                is_engine_part = False
    return engine_part_sum


def _safe_index(schematic, row, col):
    if (row < 0 or col < 0 or
            row >= len(schematic) or col >= len(schematic[row])):
        return "."
    else:
        return schematic[row][col]


DIRECTIONS = [
        (0, 1), # right
        (0, -1), # left
        (1, 0), # down
        (-1, 0), # up
        (1, 1), # diagonal down right
        (1, -1), # diagonal down left
        (-1, 1), # diagonal up right
        (-1, -1), # diagonal up left
    ]


def _neighbors_symbol(schematic, row, col):
    for dir_row, dir_col in DIRECTIONS:
        char = _safe_index(schematic, row + dir_row, col + dir_col)
        if char != "." and not char.isnumeric():
            return True
    return False


def part2(input_file):
    schematic = [line.strip() for line in input_file.readlines()]
    star_mappings = {}
    for row in range(len(schematic)):
        curr_num = ""
        is_engine_part = False
        star_coords = None
        for col in range(len(schematic[row])):
            char = schematic[row][col]
            if char.isnumeric():
                curr_num += char
                neighbors, coords = _neighbors_star(schematic, row, col)
                if not is_engine_part and neighbors:
                    is_engine_part = True
                    star_coords = coords
                if is_engine_part and not _safe_index(schematic, row, col + 1).isnumeric():
                    if star_coords not in star_mappings:
                        star_mappings[star_coords] = []
                    star_mappings[star_coords].append(int(curr_num))
            else:
                curr_num = ""
                is_engine_part = False
                star_coords = None
    gear_ratio_sum = 0
    for _, nums in star_mappings.items():
        if len(nums) == 2:
            gear_ratio_sum += nums[0] * nums[1]
    return gear_ratio_sum


# based on the input, each number can neighbor at most 1 star
def _neighbors_star(schematic, row, col):
    for dir_row, dir_col in DIRECTIONS:
        char = _safe_index(schematic, row + dir_row, col + dir_col)
        if char == "*":
            return True, (row + dir_row, col + dir_col)
    return False, None
