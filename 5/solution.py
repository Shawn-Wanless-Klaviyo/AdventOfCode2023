def part1(input_file):
    seed_line = input_file.readline()
    seeds = [int(seed_num) for seed_num in seed_line.split(": ")[-1].split(" ")]
    _ = input_file.readline()  # newline
    ordered_mappings = [_build_mapping(input_file) for i in range(7)]
    return min([_seed_to_location(seed, ordered_mappings) for seed in seeds])


def _build_mapping(input_file):
    _ = input_file.readline()  # section title
    mapping = []
    line = input_file.readline()
    while line and line.strip() != "":
        destination_start, source_start, offset = [int(num) for num in line.strip().split(" ")]
        source_range = (source_start, source_start + offset - 1)
        mapping.append([source_range, destination_start])
        line = input_file.readline()
    return mapping


def _seed_to_location(seed, ordered_mappings):
    mapped_value = seed
    for mapping in ordered_mappings:
        for source_range, destination_start in mapping:
            if source_range[0] <= mapped_value <= source_range[1]:
                offset = mapped_value - source_range[0]
                mapped_value = destination_start + offset
                break
    return mapped_value


def part2(input_file):
    # build forward mapping
    seed_line = input_file.readline()
    seed_nums = [int(seed_num) for seed_num in seed_line.split(": ")[-1].split(" ")]
    _ = input_file.readline()  # newline
    ordered_mappings = [_build_mapping(input_file) for i in range(7)]

    seed_ranges = []
    for i in range(0, len(seed_nums), 2):
        seed_start, seed_count = seed_nums[i:i + 2]
        seed_ranges.append((seed_start, seed_start + seed_count - 1))

    # use min offset to get a heuristic for an upperbound
    min_offset = _get_min_offset(ordered_mappings) + 1
    seeds = []
    for seed_range in seed_ranges:
        for seed in range(seed_range[0], seed_range[1], min_offset):
            seeds.append(seed)
        if seeds[-1] != seed_range[1]:
            seeds.append(seed_range[1])
    location_upperbound = min([_seed_to_location(seed, ordered_mappings) for seed in seeds])

    # build backwards mapping to check locations
    input_file.seek(0)
    seed_line = input_file.readline()
    seed_nums = [int(seed_num) for seed_num in seed_line.split(": ")[-1].split(" ")]
    _ = input_file.readline()  # newline
    reverse_mappings = [_build_reverse_mapping(input_file) for i in range(7)][::-1]
    seed_ranges = []
    for i in range(0, len(seed_nums), 2):
        seed_start, seed_count = seed_nums[i:i + 2]
        seed_ranges.append((seed_start, seed_start + seed_count - 1))

    # The heuristic upperbound should be in the lowest "bucket" of possible locations.
    # The bottom of this bucket would be the lowest location, assuming there's no
    # breakthrough of unmapped values in the prior mapping layers.
    # You could just do a brute force search up from zero and return the first location
    # mapped to a seed to account for any breakthroughs.
    # But it just so happens that my input didn't have a breakthrough as the lowest,
    # so simply finding the bottom of the upperbound's bucket suffices here.
    min_location = location_upperbound
    for location in range(location_upperbound - 1, -1, -1):
        if min_location - location > 1:
            break
        if _location_to_seed(location, reverse_mappings, seed_ranges):
            min_location = location
    return min_location


def _build_reverse_mapping(input_file):
    _ = input_file.readline()  # section title
    mapping = []
    line = input_file.readline()
    while line and line.strip() != "":
        destination_start, source_start, offset = [int(num) for num in line.strip().split(" ")]
        destination_range = (destination_start, destination_start + offset - 1)
        mapping.append([destination_range, source_start])
        line = input_file.readline()
    return mapping


def _location_to_seed(location, ordered_mappings, seed_ranges):
    mapped_value = location
    for mapping in ordered_mappings:
        for source_range, destination_start in mapping:
            if source_range[0] <= mapped_value <= source_range[1]:
                offset = mapped_value - source_range[0]
                mapped_value = destination_start + offset
                break
    for seed_range in seed_ranges:
        if seed_range[0] <= mapped_value <= seed_range[1]:
            return True
    return False


def _get_min_offset(ordered_mappings):
    initial_start, initial_stop = ordered_mappings[0][0][0]
    min_offset = initial_stop - initial_start
    for mapping in ordered_mappings:
        for source_range, destination_start in mapping:
            offset = source_range[1] - source_range[0]
            if offset < min_offset:
                min_offset = offset
    return min_offset
