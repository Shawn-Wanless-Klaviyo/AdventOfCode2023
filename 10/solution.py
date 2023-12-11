def part1(input_file):
    pipe_grid = []
    start_point = None
    for line in input_file.readlines():
        pipe_grid.append([char for char in line.strip()])
        if not start_point:
            find_S = line.find("S")
            if find_S != -1:
                start_point = (len(pipe_grid) - 1, find_S)
    steps = 1
    row_diff, col_diff = next(_get_first_tile(pipe_grid, start_point))
    curr_row, curr_col = start_point[0] + row_diff, start_point[1] + col_diff
    curr_pipe = pipe_grid[curr_row][curr_col]
    while curr_pipe != "S":
        steps += 1
        row_diff, col_diff = direction_mapping[curr_pipe][(row_diff, col_diff)]
        curr_row, curr_col = curr_row + row_diff, curr_col + col_diff
        curr_pipe = pipe_grid[curr_row][curr_col]
    return steps // 2


def _get_first_tile(grid, start_point):
    start_row, start_col = start_point
    for i in range(-1, 2):
        for j in range(-1, 2):
            if abs(i) == abs(j):
                continue
            grid_symbol = grid[start_row + i][start_col + j]
            if grid_symbol not in direction_mapping:
                continue
            if (i, j) not in direction_mapping[grid_symbol]:
                continue
            yield i, j


# direction_mapping item format is also follows:
# pipe_character: {
#     coord_diff_from_previous_tile: coord_diff_to_get_to_next_tile
# }
# coords = (row, col)
direction_mapping = {
    "|": {
        (-1, 0): (-1, 0),  # inbound up, outbound up
        (1, 0): (1, 0)  # inbound down, outbound down
    },
    "-": {
        (0, -1): (0, -1),  # inbound left, outbound left
        (0, 1): (0, 1)  # inbound right, outbound right
    },
    "F": {
        (-1, 0): (0, 1),  # inbound up, outbound right
        (0, -1): (1, 0)  # inbound left, outbound down
    },
    "7": {
        (-1, 0): (0, -1),  # inbound up, outbound left
        (0, 1): (1, 0),  # inbound right, outbound down
    },
    "L": {
        (1, 0): (0, 1),  # inbound down, outbound right
        (0, -1): (-1, 0)  # inbound left, outbound up
    },
    "J": {
        (1, 0): (0, -1),  # inbound down, outbound left
        (0, 1): (-1, 0),  # inbound right, outbound up
    }
}


def part2(input_file):
    pipe_grid = []
    start_point = None
    for line in input_file.readlines():
        pipe_grid.append([char for char in line.strip()])
        if not start_point:
            find_S = line.find("S")
            if find_S != -1:
                start_point = (len(pipe_grid) - 1, find_S)

    is_loop_grid = [[False for item in row] for row in pipe_grid]
    is_loop_grid[start_point[0]][start_point[1]] = True

    start_neighbors = [tile for tile in _get_first_tile(pipe_grid, start_point)]

    row_diff, col_diff = start_neighbors[0]
    curr_row, curr_col = start_point[0] + row_diff, start_point[1] + col_diff
    curr_pipe = pipe_grid[curr_row][curr_col]
    while curr_pipe != "S":
        is_loop_grid[curr_row][curr_col] = True
        row_diff, col_diff = direction_mapping[curr_pipe][(row_diff, col_diff)]
        curr_row, curr_col = curr_row + row_diff, curr_col + col_diff
        curr_pipe = pipe_grid[curr_row][curr_col]

    for symbol, offset_dicts in direction_mapping.items():
        both = True
        for _, val in offset_dicts.items():
            if val not in start_neighbors:
                both = False
                break
        if both:
            pipe_grid[start_point[0]][start_point[1]] = symbol
            break

    for row in range(len(pipe_grid)):
        for col in range(len(pipe_grid[row])):
            if not is_loop_grid[row][col]:
                pipe_grid[row][col] = "."

    in_loop_tiles = 0
    boundaries = {"|", "7", "F"}
    for row in range(len(pipe_grid)):
        in_loop = False
        for col in range(len(pipe_grid[row])):
            curr_symbol = pipe_grid[row][col]
            if is_loop_grid[row][col] and curr_symbol in boundaries:
                in_loop = not in_loop
            elif not is_loop_grid[row][col] and in_loop:
                in_loop_tiles += 1
    return in_loop_tiles
