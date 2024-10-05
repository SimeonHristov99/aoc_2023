from __future__ import annotations

from typing import Sequence, TypeVar

T = TypeVar('T')


def valid_coords(i: int, j: int, matrix: Sequence[Sequence[T]]) -> bool:
    """
    Checks whether the coordinates (i, j) are valid in the supplied matrix.

    Args:
        i (int): The row index.
        j (int): The column index.
        matrix (Sequence[Sequence[T]]): The container in which to
            check the validity of the coordinates.

    Returns:
        bool: Whether indexing can be called on
            matrix with the coordinates (i, j).
    """
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def get_lines(filename: str) -> list[str]:
    """
    Parses the lines of a text file.

    Args:
        filename (str): Path to the file for which to return the lines.

    Returns:
        list[str]: A list in which each element is a
            string representing the contents of each line in the provided file.
    """
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines
