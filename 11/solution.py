def part1(input_file, empty_length=2):
    expanded_universe = []

    empty_rows = []
    for i, line in enumerate(input_file.readlines()):
        tidied_line = [char for char in line.strip()]
        expanded_universe.append(tidied_line)
        if "#" not in tidied_line:
            empty_rows.append(i)

    empty_cols = []
    for col in range(len(expanded_universe[0])):
        galaxy_seen = False
        for row in range(len(expanded_universe)):
            if expanded_universe[row][col] == "#":
                galaxy_seen = True
                break
        if not galaxy_seen:
            empty_cols.append(col)

    galaxies = []
    for row in range(len(expanded_universe)):
        for col in range(len(expanded_universe[row])):
            if expanded_universe[row][col] == "#":
                galaxies.append((row, col))

    sum_of_paths = 0
    for i, coords in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            sum_of_paths += _manhattan_dist(galaxies[i], galaxies[j],
                                            empty_rows, empty_cols,
                                            empty_length)
    return sum_of_paths


def _manhattan_dist(coordA, coordB, empty_rows, empty_cols, empty_length):
    row_dist = abs(coordA[0] - coordB[0])
    col_dist = abs(coordA[1] - coordB[1])
    for empty_row in empty_rows:
        if coordA[0] < empty_row < coordB[0]:
            row_dist += empty_length - 1
    for empty_col in empty_cols:
        if (coordA[1] < empty_col < coordB[1] or
                coordA[1] > empty_col > coordB[1]):
            col_dist += empty_length - 1
    return row_dist + col_dist


def part2(input_file):
    return part1(input_file, empty_length=1_000_000)
