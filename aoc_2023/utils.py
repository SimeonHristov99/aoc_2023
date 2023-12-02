def get_lines(filename: str) -> list[str]:
    """
    Parses the lines of a text file.

    Args:
        filename (str): Path to the file for which to return the lines.

    Returns:
        list[str]: A list in which each element is a string representing the contents of each line in the provided file.
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines
