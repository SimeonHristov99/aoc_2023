from queue import Queue


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
    starting_positions = [node for node in map_ if node.endswith('A')]

    directions_idxs = [
        0 if direction == 'L' else 1 for direction in directions
    ]
    len_directions_idxs = len(directions_idxs)
    print(len_directions_idxs)
    num_steps = 0

    while not all(node.endswith('Z') for node in starting_positions):
        print(starting_positions)
        nodes_done = [
            node for node in starting_positions if node.endswith('Z')
        ]
        # print(nodes_done)
        if len(nodes_done) == 6:
            print('Jello')
        direction = directions_idxs[num_steps % len_directions_idxs]
        starting_positions = [
            map_[node][direction] for node in starting_positions
        ]
        num_steps += 1
        print(num_steps)

    return num_steps


def part1(filename: str) -> int:
    directions, map_ = parse_input(filename)
    return num_steps(directions, map_)


def bfs(map_: dict[str, tuple[str, str]],
        root: str) -> list[tuple[list[str], str]]:
    result = []

    queue = Queue()
    queue.put(([root], ''))

    seen = set()

    while not queue.empty():
        path, directions = queue.get()

        if path[0].endswith('Z'):
            result.append((path, directions))

        child1, child2 = map_[path[0]]

        if child1 not in seen and child2 not in seen:
            queue.put(([child1] + path, 'L' + directions))
            queue.put(([child2] + path, 'R' + directions))
        elif child1 in seen and child2 not in seen:
            queue.put(([child2] + path, 'R' + directions))
        elif child1 not in seen and child2 in seen:
            queue.put(([child1] + path, 'L' + directions))

        seen.add(path[0])

    return result


def part2(filename: str) -> int:
    directions, map_ = parse_input(filename)
    return num_ghost_steps(directions, map_)


def main() -> None:
    # print(f'Part 1, Sample: {part1("aoc_2023/day08/sample1.txt")}')  # 2
    # print(f'Part 1, Sample: {part1("aoc_2023/day08/sample2.txt")}')  # 6
    # print(f'Part 1, Input: {part1("aoc_2023/day08/input.txt")}')  # 16409

    # print(f'Part 2, Sample: {part2("aoc_2023/day08/sample3.txt")}')  # 6
    print(f'Part 2, Input: {part2("aoc_2023/day08/input.txt")}')


if __name__ == '__main__':
    main()
