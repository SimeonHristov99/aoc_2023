def parse(filepath: str) -> list[list[str]]:
    with open(filepath, 'r') as file_fp:
        lines = file_fp.read().splitlines()
    return [list(line) for line in lines]


def transpose(xss: list[list[str]]) -> list[list[str]]:
    result = []
    num_cols = len(xss[0])
    for col_idx in range(num_cols):
        result.append([xs[col_idx] for xs in xss])
    return result


def get_empty_lines(universe: list[list[str]], axis: int) -> list[int]:
    if axis == 0:
        return [idx for idx, row in enumerate(universe) if '#' not in row]
    if axis == 1:
        return [idx for idx, row in enumerate(transpose(universe)) if '#' not in row]
    raise ValueError(f'Axis={axis} is not supported. The axis value must be either 0 or 1.')


def expand(coords: list[tuple[int, int]], coefficient_of_expansion: int, empty_row_idxs: list[int],
           empty_col_idxs: list[int]) -> list[tuple[int, int]]:
    annotated_coords = [(x, y, sum(1
                                   for row in empty_row_idxs
                                   if row < x), sum(1
                                                    for col in empty_col_idxs
                                                    if col < y))
                        for x, y in coords]
    expanded_coords = [(x + num_expansions_x * coefficient_of_expansion,
                        y + num_expansions_y * coefficient_of_expansion)
                       for x, y, num_expansions_x, num_expansions_y in annotated_coords]
    return expanded_coords


def get_galaxy_coordinates(universe: list[list[str]]) -> list[tuple[int, int]]:
    galaxy_coordinates = []
    num_rows = len(universe)
    num_cols = len(universe[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if universe[i][j] == '#':
                galaxy_coordinates.append((i, j))
    return galaxy_coordinates


def get_pairs(coords: list[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    result = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            result.append((coords[i], coords[j]))
    return result


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def expand_and_sum_total(filename: str, coefficient_of_expansion: int) -> int:
    universe = parse(filename)
    initial_coords = get_galaxy_coordinates(universe)
    if coefficient_of_expansion > 1:
        expanded = expand(initial_coords, coefficient_of_expansion - 1,
                          get_empty_lines(universe, 0), get_empty_lines(universe, 1))
    else:
        expanded = expand(initial_coords, coefficient_of_expansion, get_empty_lines(universe, 0),
                          get_empty_lines(universe, 1))
    return sum(manhattan_distance(p1, p2) for p1, p2 in get_pairs(expanded))


def part1(filename: str) -> int:
    return expand_and_sum_total(filename, 1)


def part2(filename: str) -> int:
    return expand_and_sum_total(filename, 1_000_000)


def main() -> None:
    print(f'Part 1, Sample: {part1("./aoc_2023/day11/sample.txt")}')
    print(f'Part 1, Input: {part1("./aoc_2023/day11/input.txt")}')

    print(f'Part 2, Sample: {part2("./aoc_2023/day11/sample.txt")}')
    print(f'Part 2, Input: {part2("./aoc_2023/day11/input.txt")}')


if __name__ == '__main__':
    main()
