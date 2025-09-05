def parse_input(filename: str) -> list[list[str]]:
    """
    Parse the puzzle input file into a list of patterns.
    :param filename str: Path to the input file.
    :returns list[list[str]]: A list of patterns, where each pattern is represented as a list of strings.
    """
    result = []
    patterns = ''
    with open(filename, 'r') as fp:
        patterns = fp.read()
    result = [pattern.split() for pattern in patterns.split('\n\n')]
    return result


class Summarizer:

    def __init__(self, pattern: list[str]) -> None:
        """
        Instantiate an object and save a pattern in its state.
        """
        self.pattern = pattern

    def summarize(self) -> int:
        """
        Create a summary of the saved pattern.
        :returns int: The number of columns to the left of each vertical line of reflection + 100 multiplied by the number of rows above each horizontal line of reflection
        """
        return 0

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
