import enum

from joblib import Parallel, delayed


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


class Direction(enum.Enum):
    ROWS = 1
    COLS = 2


class Summarizer:

    def __init__(self, pattern: list[str]) -> None:
        """
        Instantiate an object and save a pattern in its state.
        """
        self.pattern = pattern

    def create_reflection_maps(
            self) -> tuple[dict[int, list[tuple[int, int]]], dict[int, list[tuple[int, int]]]]:
        """
        Creates all the possible rows and columns to check for each possible line.
        :returns tuple[dict[int, list[tuple[int, int]]], dict[int, list[tuple[int, int]]]]: A tuple with the horizontal and vertical indices to check.
        """
        num_rows = len(self.pattern)
        num_cols = len(self.pattern[0])

        lines_horizontal: dict[int, list[tuple[int, int]]] = {}
        lines_vertical: dict[int, list[tuple[int, int]]] = {}

        for line_container, num_lines in [(lines_horizontal, num_rows),
                                          (lines_vertical, num_cols)]:
            for i in range(num_lines):
                ii = i
                jj = i + 1
                possibilities = []
                while ii >= 0 and jj < num_lines:
                    possibilities.append((ii, jj))
                    ii -= 1
                    jj += 1
                if len(possibilities) > 0:
                    line_container[i] = possibilities

        return (lines_horizontal, lines_vertical)

    def forms_reflection_column(self, columns_to_check: list[tuple[int, int]], with_smudge: bool) -> bool:
        """
        Returns whether a collection of columns form a reflection (with or without a smudge).
        :param list[tuple[int, int]] columns_to_check: The indices of the columns to check for reflection.
        :param bool with_smudge: Whether to compare the columns allowing for one smudge.
        :returns bool: Whether the columns form a reflection.
        """
        return False

    def summarize_column(self, line_number: int) -> int:
        """
        Checks whether the line forms a reflection and, if it does, returns a summary.
        :param int line_number: The line that is to be checked.
        :returns int: Zero if the line does not form a reflection, otherwise the number of columns to the left of the line.
        """
        columns_to_check = self.lines_vertical[line_number]

        for left, right in columns_to_check:
            for i in range(len(self.pattern)):
                if self.pattern[i][left] != self.pattern[i][right]:
                    return 0

        return line_number + 1

    def summarize_row(self, line_number: int) -> int:
        """
        Checks whether the line forms a reflection and, if it does, returns a summary.
        :param int line_number: The line that is to be checked.
        :returns int: Zero if the line does not form a reflection, otherwise 100 multiplied by the number of rows above the reflection.
        """
        rows_to_check = self.lines_horizontal[line_number]
        if any(self.pattern[left] != self.pattern[right] for left, right in rows_to_check):
            return 0
        return (line_number + 1) * 100

    def summarize_direction(self, direction: Direction) -> int:
        """
        Creates a summary either by columns or by rows.
        :param direction Direction: Dictates which axis is summarized.
        :returns int: When direction='rows', then returns 100 multiplied by the number of rows above the horizontal line of reflection. Else, the number of columns to the left of the vertical line of reflection.
        """
        if direction == Direction.ROWS:
            return sum(
                Parallel(n_jobs=-1,
                         prefer="threads")(delayed(self.summarize_row)(line)
                                           for line in range(len(self.lines_horizontal))))
        return sum(
            Parallel(n_jobs=-1, prefer="threads")(delayed(self.summarize_column)(line)
                                                  for line in range(len(self.lines_vertical))))

    def summarize(self) -> int:
        """
        Create a summary of the saved pattern.
        :returns int: The number of columns to the left of each vertical line of reflection + 100 multiplied by the number of rows above each horizontal line of reflection
        """
        self.lines_horizontal, self.lines_vertical = self.create_reflection_maps()
        return sum(
            Parallel(n_jobs=2)(delayed(self.summarize_direction)(getattr(Direction, direction))
                               for direction in ['ROWS', 'COLS']))


def part1(filename: str) -> int:
    """
    Compute the summary of the notes.
    :param filename str: Path to the input file.
    :returns int: The summary of the notes.
    """
    patterns = parse_input(filename)
    summarizers = [Summarizer(pattern) for pattern in patterns]
    summary = sum(
        Parallel(n_jobs=-1)(delayed(summarizer.summarize)() for summarizer in summarizers))
    return summary


def main() -> None:
    """Executes part 1 on both the sample and actual input files, printing the results to standard output."""
    print(f'Part 1, Sample: {part1("aoc_2023/day13/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day13/input.txt")}')


if __name__ == '__main__':
    main()
