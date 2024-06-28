def parse_input(filename: str) -> list[tuple[int, int]]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    return list(zip(times, distances))


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
    print('Hello, world')
    return 42


def part2(filename: str) -> int:
    print('Hello, world')
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day05/sample.txt")}')  # 35
    # print(f'Part 1, Input: {part1("aoc_2023/day05/input.txt")}')

    # print(f'Part 2, Sample: {part2("aoc_2023/day05/sample.txt")}')
    # print(f'Part 2, Input: {part2("aoc_2023/day05/input.txt")}')


if __name__ == '__main__':
    main()
