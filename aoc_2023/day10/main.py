def find_one(matrix: list[list[str]]) -> tuple[int, int]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 'S':
                return (i, j)
    raise NotImplementedError('Coordinates of starting point not found.')


def up(
    coords: tuple[int, int], stack: list[list[tuple[int, int]]],
    seen: set[tuple[int, int]], path: list[tuple[int, int]]
) -> list[list[tuple[int, int]]]:
    x, y = coords
    if 0 < x:
        next_ = (x - 1, y)
        if next_ not in seen:
            stack.append(path + [next_])
    return stack


def num_steps_farthest(
    matrix: list[list[str]], start_coords: tuple[int, int]
) -> int:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    stack = [[start_coords]]
    seen = set()
    max_len_path = 0

    while len(stack) > 0:
        path = stack.pop()
        x, y = path[-1]

        max_len_path = max(max_len_path, len(path))

        seen.add((x, y))

        if matrix[x][y] == '|':  # only up and down
            ...
        elif matrix[x][y] == '-':  # only left and right
            ...
        elif matrix[x][y] == 'L':  # only up and right
            ...
        elif matrix[x][y] == 'J':  # only up and left
            ...
        elif matrix[x][y] == '7':  # only down and left
            ...
        elif matrix[x][y] == 'F':  # only down and right
            ...
        else:
            continue

        if 0 < y:
            next_ = (x, y - 1)  # left
            if next_ not in seen:
                stack.append(path + [next_])
        if y < num_cols - 1:
            next_ = (x, y + 1)  # right
            if next_ not in seen:
                stack.append(path + [next_])

        if x < num_rows - 1:
            next_ = (x + 1, y)  # down
            if next_ not in seen:
                stack.append(path + [next_])

    return max_len_path


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
