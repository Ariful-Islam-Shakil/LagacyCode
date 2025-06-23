import string
import math
import pandas as pd
from typing import Dict

def main():
    print(string_utils.say_hello("Python 3.12 User"))

    title = math_utils.fetch_website_title("https://www.example.com")
    print(f"Website Title: {title}")

    mean_val = math_utils.calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = math_utils.create_dataframe()
    print("DataFrame:\n", df)

    text = "Python is fun and Python is powerful"
    word_count = string_utils.count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Generated Range Squares:", math_utils.generate_range(5))

    print("StringIO Buffer Output:\n" + string_utils.string_io_example())

    print("Dictionary Iteration Output:")
    for line in string_utils.dictionary_iteration():
        print(line)

    print("Exception Handling Test:", math_utils.exception_handling_demo())

if __name__ == '__main__':
    main()

# utils/string_utils.py
from io import StringIO
from typing import Dict

def say_hello(name: str) -> str:
    return f"Hello, {name}!"

def count_words(text: str) -> Dict[str, int]:
    words = text.split()
    word_count: Dict[str, int] = {}
    for word in words:
        word = word.strip('.,!?"\'')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def string_io_example() -> str:
    buffer = StringIO()
    buffer.write("Hello, World!")
    buffer.seek(0)
    return buffer.read()

def dictionary_iteration() -> list:
    dictionary = {"key1": "value1", "key2": "value2"}
    return [f"{key}: {value}" for key, value in dictionary.items()]

# utils/math_utils.py
import pandas as pd
import random

def fetch_website_title(url: str) -> str:
    # Simulate fetching website title
    return "Example Website Title"

def calculate_mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)

def create_dataframe() -> pd.DataFrame:
    data = {
        "Name": ["John", "Mary", "David"],
        "Age": [25, 31, 42]
    }
    return pd.DataFrame(data)

def generate_range(n: int) -> list:
    return [i ** 2 for i in range(n)]

def exception_handling_demo() -> str:
    try:
        raise Exception("Test Exception")
    except Exception as e:
        return str(e)