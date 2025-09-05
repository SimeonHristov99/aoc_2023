def parse_input(filename: str) -> list[list[str]]:
    """
    Parse the puzzle input file into a list of patterns.
    :param filename str: Path to the input file.
    :returns list[list[str]]: A list of patterns, where each pattern is represented as a list of strings.
    """
    patterns = []
    with open(filename, 'r') as fp:
        patterns = fp.read()
    patterns = [pattern.split() for pattern in patterns.split('\n\n')]
    return patterns


def part1(filename: str) -> int:
    """
    Compute the summary of the notes.
    :param filename str: Path to the input file.
    :returns int: The summary of the notes.
    """
    return 42


def main() -> None:
    """Executes part 1 on both the sample and actual input files, printing the results to standard output."""
    print(f'Part 1, Sample: {part1("aoc_2023/day_template/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day_template/input.txt")}')


if __name__ == '__main__':
    main()
