def parse_input(filename: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    directions = lines[0]
    map_ = {
        start_node: tuple(children[1:-1].split(', '))
        for line in lines[2:]
        for start_node, children in [line.split(' = ')]
    }
    return directions, map_


def num_steps(directions: str, map_: dict[str, tuple[str, str]]) -> int:
    pos = 'AAA'
    directions_idxs = [
        0 if direction == 'L' else 1 for direction in directions
    ]
    len_directions_idxs = len(directions_idxs)
    num_steps = 0
    while pos != 'ZZZ':
        pos = map_[pos][directions_idxs[num_steps % len_directions_idxs]]
        num_steps += 1
        if pos == 'ZZZ':
            break
    return num_steps


def num_ghost_steps(directions: str, map_: dict[str, tuple[str, str]]) -> int:
    mat = [[[0] * 43] * 43] * 43
    for (l1, l2, l3) in map_:
        mat[ord(l1) - ord('0')][ord(l2) - ord('0')][ord(l3) - ord('0')] = 1

    for (l1, l2, l3) in map_:
        print(
            f"{l1}{l2}{l3} => {mat[ord(l1) - ord('0')][ord(l2) - ord('0')][ord(l3) - ord('0')]}"
        )

    for idxr, row in enumerate(mat):
        for idxc, col in enumerate(row):
            for idxe, entry in enumerate(col):
                if entry == 1:
                    print(entry, col, row)
                    # print(chr(ord('0') + idxr + 1), chr(ord('0') + idxc + 1), chr(ord('0') + idxe + 1))
                    # break
            # break
        break

    x = 5 + 6


def part1(filename: str) -> int:
    directions, map_ = parse_input(filename)
    return num_steps(directions, map_)


def part2(filename: str) -> int:
    directions, map_ = parse_input(filename)
    return num_ghost_steps(directions, map_)


def main() -> None:
    # print(f'Part 1, Sample: {part1("aoc_2023/day08/sample1.txt")}')  # 2
    # print(f'Part 1, Sample: {part1("aoc_2023/day08/sample2.txt")}')  # 6
    # print(f'Part 1, Input: {part1("aoc_2023/day08/input.txt")}')  # 16409

    print(f'Part 2, Sample: {part2("aoc_2023/day08/sample3.txt")}')  # 6
    # print(f'Part 2, Input: {part2("aoc_2023/day08/input.txt")}')


if __name__ == '__main__':
    main()
