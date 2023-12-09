from solution import part1, part2

PART1 = 1
PART2 = 1

if __name__ == '__main__':
    if PART1:
        with open("input.txt") as inputFile:
            print("Part 1:")
            print(part1(inputFile))
    if PART2:
        with open("input.txt") as inputFile:
            print("\nPart 2:")
            import time;
            start = time.perf_counter()
            print(part2(inputFile))
            stop = time.perf_counter()
            print(f"Ran in {stop - start} seconds")
