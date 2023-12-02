def remove_punctuation(input: str, characters_to_remove: set[str] = {',', '.', '!', '?', ';', ':'}) -> str:
    """
    Removes a set of characters from an input string.

    Args:
        input (str): The string from which to remove the characters.
        characters_to_remove (set[str], optional): The characters to remove from `input`. Defaults to {',', '.', '!', '?', ';', ':'}.

    Returns:
        str: A string in which there are no characters that are present in `characters_to_remove`.
    """
    result = ''.join([char for char in input if char not in characters_to_remove])
    return result


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
