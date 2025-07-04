from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """Return a greeting message with the given name.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: A greeting message with the given name.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """Count the occurrences of each word in the given text.

    Args:
        text (str): The text to count words from.

    Returns:
        Counter: A dictionary-like object with word counts.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """Demonstrate using StringIO for string buffering.

    Returns:
        str: The contents of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.x with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration() -> list[str]:
    """Iterate over a dictionary and format its key-value pairs.

    Returns:
        list[str]: A list of formatted key-value pairs.
    """
    d = {'a': 1, 'b': 2}
    result = []
    for k, v in d.items():
        result.append(f"{k} => {v}")
    return result