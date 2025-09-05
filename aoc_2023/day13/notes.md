# Day 13: Point of Incidence

## What has to be done

Find the line of reflection in each of the patterns and summarize the pattern notes.

## Part 1

### Define the function for parsing the input

- [X] Add failing tests.
- [X] Make the failing tests pass.
- [X] If the part with `Arrange` logic becomes too big, consider breaking down into functions.
- [X] Identify edge cases in the written code and write tests for them.
- [X] Ensure that all newly added functions have docstrings.
- [X] Ensure `git-hook` passes.
- [X] Create your commits. Ensure that each failed test is its own commit and make sure to write the name of the test in the commit message.
- [X] Push.

### Define the method of initializing the class `Summarizer`

- [X] Add failing tests.
- [X] Make the failing tests pass.
- [X] Ensure that all newly added functions have docstrings.
- [X] Ensure `git-hook` passes.
- [X] Create your commits. Ensure that each failed test is its own commit and make sure to write the name of the test in the commit message.
- [X] Push.

### Define a proxy method `summarize` and use it in the function `part1`

- [X] Add failing tests.
- [X] Make the failing tests pass.
- [X] Ensure `git-hook` passes.
- [X] Create your commits. Ensure that each failed test is its own commit and make sure to write the name of the test in the commit message.
- [X] Push.

### Define proxy methods `create_reflection_maps` and `summarize_direction` and use them in `summarize`

### Define the method `create_reflection_maps`

### Define proxy methods `summarize_column` and `summarize_row` and use them in `summarize_direction`

### Define the method `summarize_column`

### Define the method `summarize_row`

```python
class Summarizer:
    
    def __init__(self, pattern: list[list[str]]):
        self.pattern = pattern
    
    def create_reflection_maps(self) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        # will return the horizontal and vertical lines to check
        # ex. 0: [(0, 1)], 1: [(0, 3), (1, 2)]

    def summarize_column(self, line_number) -> int:
        # use map in self to get the columns to check
        # return a boolean expression that checks their equality
    
    def summarize_row(self, line_number) -> int:
        # use map in self to get the rows to check
        # return a boolean expression that checks their equality

    def summarize_direction(self, direction: Literal['rows', 'cols']) -> int:
        # will spawn threads to process either rows or columns
        if direction == 'rows':
            return sum(Parallel(n_jobs=-1, prefer="threads")(summarize_row[line] for line in range(len(pattern))))
        return sum(Parallel(n_jobs=-1, prefer="threads")(summarize_column[line] for line in range(len(pattern[0]))))

    def summarize(self) -> int:
        # create all possible col and row reflections as maps/dicts
        self.lines_horizontal, self.lines_vertical = create_reflection_maps()

        # run parallel processes that will try out every horizontal and vertical line and return the summary
        return sum(Parallel(n_jobs=2)([summarize_direction(direction) for direction in ['rows', 'cols']]))
```

in `part1` or wherever `Summarizer` will be used in parallel to process each pattern with `verbose=5,10,15,55` (check for usefulness)

## Part 2
