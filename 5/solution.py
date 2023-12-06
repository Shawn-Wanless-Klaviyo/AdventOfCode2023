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
    pass
