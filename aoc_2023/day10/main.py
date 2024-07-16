def find_one(matrix: list[list[str]]) -> tuple[int, int]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 'S':
                return (i, j)
    raise NotImplementedError('Coordinates of starting point not found.')


def part1(filename: str) -> int:
    return 42


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day10/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day10/input.txt")}')

    print(f'Part 2, Sample: {part2("aoc_2023/day10/sample.txt")}')
    print(f'Part 2, Input: {part2("aoc_2023/day10/input.txt")}')


if __name__ == '__main__':
    main()
