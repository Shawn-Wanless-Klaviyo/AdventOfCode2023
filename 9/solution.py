def part1(input_file, reverse=False):
    jump = -1 if reverse else 1
    res = 0
    for line in input_file.readlines():
        data = [int(num) for num in line.strip().split(" ")]
        res += _extrapolate(data[::jump])
    return res


def _extrapolate(data):
    sequences = [data]
    while not _all_same(sequences[-1]):
        next_sequence = []
        for i in range(1, len(sequences[-1])):
            next_sequence.append(sequences[-1][i] - sequences[-1][i - 1])
        sequences.append(next_sequence)
    next_num = sequences[-1][-1]
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + next_num)
        next_num = sequences[i][-1]
    return next_num


def _all_same(sequence):
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            return False
    return True


def part2(input_file):
    return part1(input_file, reverse=True)
