# Day 13: Point of Incidence

## What has to be done

Find the line of reflection in each of the patterns and summarize the pattern notes.

## Part 1

```python
class Summarizer:
    
    def __init__(self, pattern: list[list[str]]):
        self.pattern = pattern
    
    def create_reflection_maps(self) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        # will return the horizontal and vertical lines to check

    def summarize_column(self, line_number) -> int:
        # use map in self to get the columns to check
        # return a boolean expression that checks their equality
    
    def summarize_row(self, line_number) -> int:
        # use map in self to get the rows to check
        # return a boolean expression that checks their equality

    def summarize_direction(self, direction: Literal['rows', 'cols']) -> int:
        # will spawn threads to process either rows or columns
        return sum(Parallel(n_jobs=-1, prefer="threads")([summarize_direction(direction) for direction in ['rows', 'cols']]))

    def summarize(self) -> int:
        # create all possible col and row reflections as maps/dicts: store them in self
        lines_horizontal, lines_vertical = create_reflection_maps()

        # run parallel processes that will try out every horizontal and vertical line and return the summary
        return sum(Parallel(n_jobs=2)([summarize_direction(direction) for direction in ['rows', 'cols']]))
```

in `part1` or wherever `Summarizer` will be used in parallel to process each pattern with `verbose=5,10,15,55` (check for usefulness)

## Part 2
