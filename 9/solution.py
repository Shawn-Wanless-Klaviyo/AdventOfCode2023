def part1(input_file, reverse=False):
    res = 0
    for line in input_file.readlines():
        data = [int(num) for num in line.strip().split(" ")]
        res += _extrapolate_rec(data[::-1 if reverse else 1])
    return res


def _extrapolate_rec(data):
    if not any(data):
        return 0
    next_num = _extrapolate_rec([data[i] - data[i - 1] for i in range(1, len(data))])
    return data[-1] + next_num


def part2(input_file):
    return part1(input_file, reverse=True)
