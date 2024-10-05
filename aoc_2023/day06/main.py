import math


def parse_input(filename: str) -> list[tuple[int, int]]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    return list(zip(times, distances))


def parse_input_part2(filename: str) -> list[tuple[int, int]]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    time = int(''.join(lines[0].split(': ')[1].split()))
    distance = int(''.join(lines[1].split(': ')[1].split()))
    return time, distance


def get_bigger_distances(time: int, threshold: int) -> int:
    """
    Returns the number of ways to get a distance larger than a specified threshold.

    Makes use of the formula: `s = v * t`.
    """
    acc = 0
    time_halved = time // 2

    while time_halved >= 0 and time_halved * (time - time_halved) > threshold:
        acc += 1
        time_halved -= 1

    return acc * 2 - (1 if time % 2 == 0 else 0)


def part1(filename: str) -> int:
    entries = parse_input(filename)
    num_bigger_distances = [get_bigger_distances(time, threshold) for time, threshold in entries]
    return math.prod(num_bigger_distances)


def part2(filename: str) -> int:
    return get_bigger_distances(*parse_input_part2(filename))


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day06/sample.txt")}')  # 288
    print(f'Part 1, Input: {part1("aoc_2023/day06/input.txt")}')  # 293046

    print(f'Part 2, Sample: {part2("aoc_2023/day06/sample.txt")}')  # 71503
    print(f'Part 2, Input: {part2("aoc_2023/day06/input.txt")}')  # 35150181


if __name__ == '__main__':
    main()
