import functools


def parse_input(filename: str) -> list[list[str]]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return [list(line) for line in lines]


def find_start(matrix: list[list[str]]) -> tuple[int, int]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 'S':
                return (i, j)
    raise NotImplementedError('Coordinates of starting point not found.')


def up(coords: tuple[int, int], stack: list[list[tuple[int, int]]], seen: set[tuple[int, int]],
       path: list[tuple[int, int]]):
    x, y = coords
    next_ = (x - 1, y)
    if 0 < x and next_ not in seen:
        stack.append(path + [next_])


def down(coords: tuple[int, int], stack: list[list[tuple[int, int]]], seen: set[tuple[int, int]],
         path: list[tuple[int, int]], num_rows: int):
    x, y = coords
    next_ = (x + 1, y)
    if x < num_rows - 1 and next_ not in seen:
        stack.append(path + [next_])


def left(coords: tuple[int, int], stack: list[list[tuple[int, int]]], seen: set[tuple[int, int]],
         path: list[tuple[int, int]]):
    x, y = coords
    next_ = (x, y - 1)
    if 0 < y and next_ not in seen:
        stack.append(path + [next_])


def right(coords: tuple[int, int], stack: list[list[tuple[int, int]]], seen: set[tuple[int, int]],
          path: list[tuple[int, int]], num_cols: int):
    x, y = coords
    next_ = (x, y + 1)
    if y < num_cols - 1 and next_ not in seen:
        stack.append(path + [next_])


def initialize_stack(matrix: list[list[str]],
                     start_coords: tuple[int, int]) -> list[list[tuple[int, int]]]:
    result = []
    x, y = start_coords
    if 0 < y and matrix[x][y - 1] == '-':  # left
        result.append([start_coords, (x, y - 1)])
    if 0 < x and matrix[x - 1][y] in {'|', 'F'}:  # up
        result.append([start_coords, (x - 1, y)])
    if x < len(matrix) - 1 and matrix[x + 1][y] in {'|', 'J'}:  # down
        result.append([start_coords, (x + 1, y)])
    if y < len(matrix[0]) - 1 and matrix[x][y + 1] in {'-', '7'}:  # right
        result.append([start_coords, (x, y + 1)])
    return result


def num_steps_farthest(matrix: list[list[str]], start_coords: tuple[int, int]) -> tuple[int, list]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    stack = initialize_stack(matrix, start_coords)
    seen = set()
    lens = []
    paths = []

    while len(stack) > 0:
        path = stack.pop()
        x, y = path[-1]

        if (x, y) == start_coords:
            lens.append(len(path))
            paths.append(path)
            continue

        seen.add((x, y))

        if matrix[x][y] == '|':  # only up and down
            up((x, y), stack, seen, path)
            down((x, y), stack, seen, path, num_rows)
        elif matrix[x][y] == '-':  # only left and right
            left((x, y), stack, seen, path)
            right((x, y), stack, seen, path, num_cols)
        elif matrix[x][y] == 'L':  # only up and right
            up((x, y), stack, seen, path)
            right((x, y), stack, seen, path, num_cols)
        elif matrix[x][y] == 'J':  # only up and left
            up((x, y), stack, seen, path)
            left((x, y), stack, seen, path)
        elif matrix[x][y] == '7':  # only down and left
            down((x, y), stack, seen, path, num_rows)
            left((x, y), stack, seen, path)
        elif matrix[x][y] == 'F':  # only down and right
            down((x, y), stack, seen, path, num_rows)
            right((x, y), stack, seen, path, num_cols)

    longest_path = functools.reduce(lambda acc, xs: xs if len(acc) < len(xs) else acc, paths, [])

    return (max(lens) - 1) // 2, longest_path


def part1(filename: str) -> int:
    matrix = parse_input(filename)
    start_coords = find_start(matrix)
    return num_steps_farthest(matrix, start_coords)


def is_encompassed(p: tuple[int, int], matrix: list[list[str]]) -> bool:
    start_coords = find_start(matrix)
    longest_path: set[tuple[int, int]] = num_steps_farthest(matrix, start_coords)[1]


def part2(filename: str) -> int:
    result = 0
    matrix = parse_input(filename)

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for x in range(num_rows):
        for y in range(num_cols):
            if is_encompassed((x, y), matrix):
                # print((x, y))
                result += 1

    return result


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day10/sample1.txt")}')  # 4
    print(f'Part 1, Sample: {part1("aoc_2023/day10/sample2.txt")}')  # 8
    print(f'Part 1, Input: {part1("aoc_2023/day10/input.txt")}')  # 6828

    # print(f'Part 2, Sample: {part2("aoc_2023/day10/sample.txt")}')
    print(f'Part 2, Input: {part2("aoc_2023/day10/input.txt")}')


if __name__ == '__main__':
    main()
