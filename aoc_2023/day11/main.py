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


def expand(universe: list[list[str]]) -> list[list[str]]:

    def helper(matrix: list[list[str]]) -> list[list[str]]:
        expanded_rows = []
        for line in matrix:
            if '#' not in line:
                expanded_rows.append(line)
            expanded_rows.append(line)
        return expanded_rows

    universe_rows_expanded = helper(universe)
    universe_columns_expanded = helper(transpose(universe_rows_expanded))
    return transpose(universe_columns_expanded)
