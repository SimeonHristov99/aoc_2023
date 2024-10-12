import copy
from typing import List, Tuple, Optional


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


def get_loop_coordinates(input_map: List[List[str]], start: Optional[Tuple[int, int]]=None) -> List[Tuple[int, int]]:
    if not start:
        start = find_start(input_map)
    
    result = [start]

    input_map_copy = copy.deepcopy(input_map)

    num_cols = len(input_map_copy[0])
    num_rows = len(input_map_copy)

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


def part2(filename: str) -> int:
    pipe_map = parse_input(filename)
    loop = get_loop_coordinates(pipe_map)

    count_ins = 0
    in_loop = False

    for i in range(len(pipe_map)):
        for j in range(len(pipe_map[0])):
            if (i, j) in loop:
                in_loop = True
            elif in_loop:
                in_loop = False

            if in_loop:
                pipe_map[i][j] = 'O'
                count_ins += 1
            else:
                pipe_map[i][j] = 'X'
    
    return count_ins


def main() -> None:
    print(f'Part 1, Sample: {part1("./aoc_2023/day10/sample.txt")}')
    print(f'Part 1, Input: {part1("./aoc_2023/day10/input.txt")}')

    print(f'Part 2, Sample: {part2("./aoc_2023/day10/sample.txt")}')
    print(f'Part 2, Input: {part2("./aoc_2023/day10/input.txt")}')


if __name__ == '__main__':
    main()
