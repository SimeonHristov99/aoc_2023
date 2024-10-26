import copy
from typing import List, Optional, Set, Tuple


def parse_input(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return [[c for c in line] for line in lines]


def find_start(pipe_map: List[List[str]]) -> Tuple[int, int]:
    for i in range(len(pipe_map)):
        for j in range(len(pipe_map[0])):
            if pipe_map[i][j] == 'S':
                return (i, j)
    return (-1, -1)


def get_loop_coordinates(input_map: List[List[str]],
                         start: Optional[Tuple[int, int]] = None) -> List[Tuple[int, int]]:
    if not start:
        start = find_start(input_map)

    result = [start]

    input_map_copy = copy.deepcopy(input_map)

    num_cols = len(input_map_copy[0])

    possible_right = {'-', 'J', '7'}
    possible_up = {'|', '7', 'F'}
    possible_left = {'-', 'L', 'F'}
    possible_down = {'|', 'L', 'J'}

    can_move = { # map pipe type to possible movements [right, up, left, down]
        '|': [False, True, False, True],
        '-': [True, False, True, False],
        'L': [True, True, False, False],
        'J': [False, True, True, False],
        '7': [False, False, True, True],
        'F': [True, False, False, True],
    }

    (x, y) = start

    if y < num_cols and input_map_copy[x][y + 1] in possible_right:
        y = y + 1
    elif x > 0 and input_map_copy[x - 1][y] in possible_up:
        x = x - 1
    elif y > 0 and input_map_copy[x][y - 1] in possible_left:
        y = y - 1
    else:
        raise ValueError('Input map does not have two connected pipes to the starting pipe.')

    while True:
        result.append((x, y))
        can_move_right, can_move_up, can_move_left, can_move_down = can_move[input_map[x][y]]
        input_map_copy[x][y] = 'X'

        if can_move_right and y < num_cols and input_map_copy[x][y + 1] in possible_right:
            y = y + 1
        elif can_move_up and x > 0 and input_map_copy[x - 1][y] in possible_up:
            x = x - 1
        elif can_move_left and y > 0 and input_map_copy[x][y - 1] in possible_left:
            y = y - 1
        elif can_move_down and input_map_copy[x + 1][y] in possible_down:
            x += 1
        else:
            break

    return result


def part1(filename: str) -> int:
    return len(get_loop_coordinates(parse_input(filename))) // 2


def to_differences(
    loop_coords: List[Tuple[int, int]]
) -> List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    loop_coords += [loop_coords[0]]
    return [(p1, p2, (p2[0] - p1[0], p2[1] - p1[1]))
            for p1, p2 in zip(loop_coords, loop_coords[1:])]


def determine_side(loop_coords: List[Tuple[int, int]]) -> str:
    num_turns_right = 0
    num_turns_left = 0
    current_direction = 'right'
    for _, _, diff in to_differences(loop_coords):
        if current_direction == 'right' and diff == (1, 0):
            num_turns_right += 1
            current_direction = 'down'
        elif current_direction == 'right' and diff == (-1, 0):
            num_turns_left += 1
            current_direction = 'up'
        elif current_direction == 'down' and diff == (0, -1):
            num_turns_right += 1
            current_direction = 'left'
        elif current_direction == 'down' and diff == (0, 1):
            num_turns_left += 1
            current_direction = 'right'
        elif current_direction == 'left' and diff == (-1, 0):
            num_turns_right += 1
            current_direction = 'up'
        elif current_direction == 'left' and diff == (1, 0):
            num_turns_left += 1
            current_direction = 'down'
        elif current_direction == 'up' and diff == (0, 1):
            num_turns_right += 1
            current_direction = 'right'
        elif current_direction == 'up' and diff == (0, -1):
            num_turns_left += 1
            current_direction = 'left'

    return 'left' if num_turns_left > num_turns_right else 'right'


def get_internal_and_border_points(differences: List[Tuple[Tuple[int, int], Tuple[int, int],
                                                           Tuple[int, int]]],
                                   side: str) -> Set[Tuple[int, int]]:
    result = set()
    previous_direction = None

    for (x, y), _, diff in differences:
        if diff == (0, 1) and side == 'right':
            if previous_direction and previous_direction == 'down':  # we have a corner (down->right)
                result.add((x, y - 1))
                result.add((x + 1, y - 1))

            result.add((x + 1, y))
            previous_direction = 'right'
        elif diff == (0, 1) and side == 'left':
            if previous_direction and previous_direction == 'up':  # we have a corner (up->right)
                result.add((x, y - 1))
                result.add((x - 1, y - 1))

            result.add((x - 1, y))
            previous_direction = 'right'
        elif diff == (0, -1) and side == 'right':
            if previous_direction and previous_direction == 'up':  # we have a corner (up->left)
                result.add((x, y + 1))
                result.add((x - 1, y + 1))

            result.add((x - 1, y))
            previous_direction = 'left'
        elif diff == (0, -1) and side == 'left':
            if previous_direction and previous_direction == 'down':  # we have a corner (down->left)
                result.add((x, y + 1))
                result.add((x + 1, y + 1))

            result.add((x + 1, y))
            previous_direction = 'left'
        elif diff == (1, 0) and side == 'right':
            if previous_direction and previous_direction == 'left':  # we have a corner (left->down)
                result.add((x - 1, y))
                result.add((x - 1, y - 1))

            result.add((x, y - 1))
            previous_direction = 'down'
        elif diff == (1, 0) and side == 'left':
            if previous_direction and previous_direction == 'right':  # we have a corner (right->down)
                result.add((x - 1, y))
                result.add((x - 1, y + 1))

            result.add((x, y + 1))
            previous_direction = 'down'
        elif diff == (-1, 0) and side == 'right':
            if previous_direction and previous_direction == 'right':  # we have a corner (right->up)
                result.add((x + 1, y))
                result.add((x + 1, y + 1))

            result.add((x, y + 1))
            previous_direction = 'up'
        elif diff == (-1, 0) and side == 'left':
            if previous_direction and previous_direction == 'left':  # we have a corner (left->up)
                result.add((x + 1, y))
                result.add((x + 1, y - 1))

            result.add((x, y - 1))
            previous_direction = 'up'

    return result


def add_inner_points(internal_to_border_points: Set[Tuple[int, int]],
                     loop_coords: List[Tuple[int, int]],
                     input_map=None) -> Set[Tuple[int, int]]:
    result = set()
    internal_to_border_points = internal_to_border_points - set(loop_coords)
    random_start = next(iter(internal_to_border_points))
    stack = [random_start]
    borders = set(loop_coords) | internal_to_border_points
    visited = set(loop_coords) | internal_to_border_points

    while len(stack) > 0:
        x, y = stack.pop()

        if (x, y) not in borders:
            result.add((x, y))
            if input_map:
                input_map[x][y] = 'X'

        for i in range(-1, 2):
            for j in range(-1, 2):
                new_point = (x + i, y + j)
                if new_point not in visited and (i, j) != (0, 0):
                    stack.append((x + i, y + j))
                    if input_map:
                        input_map[x + i][y + j] = 'Z'

        visited.add((x, y))
        if input_map:
            input_map[x][y] = 'Y'

    return (result - {random_start}) | internal_to_border_points


def part2(filename: str) -> int:
    # The key here is to use the direction.
    # On one side of the loop the points will be inside,
    # on the other side - on the outside.
    input_map = parse_input(filename)
    start_coords = find_start(input_map)
    loop_coords = get_loop_coordinates(input_map)

    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if (i, j) not in loop_coords:
                input_map[i][j] = '.'

    differences = to_differences(loop_coords)
    side = determine_side(loop_coords)
    inner_points = add_inner_points(get_internal_and_border_points(differences, side), loop_coords, input_map)
    return len(inner_points)


def main() -> None:
    # print(f'Part 1, Sample: {part1("./aoc_2023/day10/sample.txt")}')
    # print(f'Part 1, Input: {part1("./aoc_2023/day10/input.txt")}')

    # print(f'Part 2, Sample: {part2("./aoc_2023/day10/sample.txt")}')
    print(f'Part 2, Input: {part2("./aoc_2023/day10/input.txt")}')


if __name__ == '__main__':
    main()
