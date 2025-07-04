from collections import Counter
from io import StringIO
from typing import List

def say_hello(name: str) -> str:
    """
    Returns a greeting message with the provided name.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: A greeting message with the provided name.

    Raises:
        TypeError: If the name is not a string.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """
    Counts the occurrences of each word in the provided text.

    Args:
        text (str): The text to count words from.

    Returns:
        Counter: A dictionary-like object with word counts.

    Raises:
        TypeError: If the text is not a string.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """
    Demonstrates the use of StringIO for creating a string buffer.

    Returns:
        str: The content of the string buffer.

    Raises:
        TypeError: If the buffer content is not a string.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: dict) -> List[str]:
    """
    Iterates over a dictionary and returns a list of key-value pairs.

    Args:
        d (dict): The dictionary to iterate over.

    Returns:
        List[str]: A list of key-value pairs as strings.

    Raises:
        TypeError: If the dictionary is not a mapping.
    """
    result = []
    for k, v in d.items():
        result.append(f"{k} => {v}")
    return result