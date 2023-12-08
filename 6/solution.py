def part1(input_file, read_as_one_race=False):
    time_line = input_file.readline()
    distance_line = input_file.readline()
    times = [num.strip() for num in time_line.split(" ")[1:] if num]
    distances = [num.strip() for num in distance_line.split(" ")[1:] if num]
    times, distances = _build_races(times, distances, read_as_one_race)

    product_of_ways_to_win = 1
    for record_time, distance in zip(times, distances):
        ways_to_win = 0
        for wait_time in range(1, record_time):
            remaining_time = record_time - wait_time
            if remaining_time * wait_time > distance:
                ways_to_win += 1
            elif ways_to_win > 0:
                break
        product_of_ways_to_win *= ways_to_win
    return product_of_ways_to_win


def _build_races(times, distances, read_as_one_race):
    if not read_as_one_race:
        return [int(num) for num in times], [int(num) for num in distances]
    return [int("".join(times))], [int("".join(distances))]


def part2(input_file):
    return part1(input_file, read_as_one_race=True)
