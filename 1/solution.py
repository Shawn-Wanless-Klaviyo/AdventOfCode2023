def part1(input_file):
    calibration_sum = 0
    for line in input_file.readlines():
        first_digit = _find_first_num(line, 0, len(line))
        last_digit = _find_first_num(line, len(line) - 1, -1, -1)
        calibration_sum += (first_digit * 10) + last_digit
    return calibration_sum


def _find_first_num(line, start, stop, step=1):
    for i in range(start, stop, step):
        if line[i].isnumeric():
            return int(line[i])


def part2(input_file):
    calibration_sum = 0
    for line in input_file.readlines():
        first_digit = _find_first_num_with_names(line, 0, len(line))
        last_digit = _find_first_num_with_names(line, len(line) - 1, -1, -1)
        calibration_sum += (first_digit * 10) + last_digit
    return calibration_sum


def _find_first_num_with_names(line, start, stop, step=1):
    for i in range(start, stop, step):
        if line[i].isnumeric():
            return int(line[i])
        elif line[i] == "o" and line[i + 1: i + 3] == "ne":
            return 1
        elif line[i] == "t" and line[i + 1: i + 3] == "wo":
            return 2
        elif line[i] == "t" and line[i + 1: i + 5] == "hree":
            return 3
        elif line[i] == "f" and line[i + 1: i + 4] == "our":
            return 4
        elif line[i] == "f" and line[i + 1: i + 4] == "ive":
            return 5
        elif line[i] == "s" and line[i + 1: i + 3] == "ix":
            return 6
        elif line[i] == "s" and line[i + 1: i + 5] == "even":
            return 7
        elif line[i] == "e" and line[i + 1: i + 5] == "ight":
            return 8
        elif line[i] == "n" and line[i + 1: i + 4] == "ine":
            return 9
