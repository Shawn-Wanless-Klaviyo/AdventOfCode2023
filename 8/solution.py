from math import lcm


def part1(input_file):
    instructions = [0 if char == "L" else 1 for char in input_file.readline().strip()]
    _ = input_file.readline()
    mapping = {}
    for line in input_file.readlines():
        node, children_str = line.strip().split(" = ")
        children = children_str[1:-1].split(", ")
        mapping[node] = children

    steps = 0
    current_node = "AAA"
    end_node = "ZZZ"
    while current_node != end_node:
        for instruction in instructions:
            steps += 1
            current_node = mapping[current_node][instruction]
            if current_node == end_node:
                break
    return steps


def part2(input_file):
    instructions = [0 if char == "L" else 1 for char in input_file.readline().strip()]
    _ = input_file.readline()
    mapping = {}
    ends_in_A = []
    for line in input_file.readlines():
        node, children_str = line.strip().split(" = ")
        children = children_str[1:-1].split(", ")
        mapping[node] = children
        if node[-1] == "A":
            ends_in_A.append(node)

    # Assumption 1: each A-ending node has exactly one Z-ending node in its cycle
    #   True, found by checking number of unique Z-endings in each cycle
    # Assumption 2: (after noticing pattern in cycle offsets and cycle length)
    #   Each cycle starts exactly len(cycle) steps in the instructions (perfect cycles)
    cycle_offsets = {}
    current_nodes = ends_in_A[:]
    steps = 0
    while len(cycle_offsets) < len(ends_in_A):
        for instruction in instructions:
            steps += 1
            next_nodes = []
            for index, node in enumerate(current_nodes):
                next_node = mapping[node][instruction]
                if next_node[-1] == "Z":
                    if index not in cycle_offsets:
                        cycle_offsets[index] = steps
                next_nodes.append(next_node)
            current_nodes = next_nodes
    cycle_lengths = [offset for _, offset in cycle_offsets.items()]
    return lcm(*cycle_lengths)
