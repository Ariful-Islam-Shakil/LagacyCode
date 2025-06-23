# utils.py

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from io import StringIO

def fetch_website_title(url: str) -> str:
    """Get website title using requests + BeautifulSoup."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: list[float]) -> float:
    """Calculate mean using numpy."""
    return np.mean(arr)

def create_dataframe() -> pd.DataFrame:
    """Create pandas DataFrame and check if 'score' column exists."""
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    if 'score' in df.columns:
        return df
    return pd.DataFrame()

def count_words(text: str) -> Counter:
    """Count word frequency using collections.Counter."""
    words = text.lower().split()
    return Counter(words)

def say_hello(name: str) -> str:
    """Modern string formatting for greeting."""
    return f"Hello, {name}!"

def generate_range(n: int) -> list[int]:
    """Generate squares using range function."""
    return [i * i for i in range(n)]

def string_io_example() -> str:
    """StringIO example for string buffer."""
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: dict[str, int]) -> list[str]:
    """Iterate dictionary with items() method."""
    return [f"{k} => {v}" for k, v in d.items()]

def exception_handling_demo() -> str:
    """Modern exception handling."""
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {str(e)}"

# main.py

def main() -> None:
    print(say_hello("Python 3.12 User"))

    title = fetch_website_title("https://www.example.com")
    print("Website Title:", title)

    mean_val = calculate_mean([5, 15, 25])
    print("Mean Value:", mean_val)

    df = create_dataframe()
    print("DataFrame:\n", df)

    # result = utils.plot_scores()
    # print(result)

    text = "Python is fun and Python is powerful"
    word_count = count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():  # Modern dictionary iteration
        print(f"{word}: {count}")

    print("Generated Range Squares:", generate_range(5))

    print("StringIO Buffer Output:\n" + string_io_example())

    print("Dictionary Iteration Output:")
    for line in dictionary_iteration({'a': 1, 'b': 2}):
        print(line)

    print("Exception Handling Test:", exception_handling_demo())

if __name__ == '__main__':
    main()