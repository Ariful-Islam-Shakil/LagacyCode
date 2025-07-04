from typing import Dict, List, Any
from dataclasses import dataclass
from io import StringIO
from urllib.parse import urlparse
from typing import Tuple
import pandas as pd
from collections import Counter

@dataclass
class WebsiteTitle:
    title: str

class StringUtils:
    @staticmethod
    def say_hello(name: str) -> str:
        """
        Prints a greeting message.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """
        Counts the occurrences of each word in a given text.

        Args:
            text (str): The text to count words from.

        Returns:
            Dict[str, int]: A dictionary with words as keys and their counts as values.
        """
        return Counter(text.split())

    @staticmethod
    def string_io_example() -> str:
        """
        Demonstrates using StringIO for buffered output.

        Returns:
            str: A string containing the output.
        """
        buffer = StringIO()
        buffer.write("Hello, World!")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """
        Demonstrates iterating over a dictionary.

        Returns:
            List[str]: A list of dictionary key-value pairs.
        """
        dictionary = {"key1": "value1", "key2": "value2"}
        return [f"{key}: {value}" for key, value in dictionary.items()]

class MathUtils:
    @staticmethod
    def fetch_website_title(url: str) -> str:
        """
        Fetches the title of a website.

        Args:
            url (str): The URL of the website.

        Returns:
            str: The title of the website.
        """
        # Simulate fetching the title (in a real application, use a library like requests)
        return urlparse(url).path

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """
        Calculates the mean of a list of numbers.

        Args:
            numbers (List[float]): The list of numbers.

        Returns:
            float: The mean of the numbers.
        """
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """
        Creates a sample DataFrame.

        Returns:
            pd.DataFrame: A sample DataFrame.
        """
        return pd.DataFrame({
            "A": [1, 2, 3],
            "B": [4, 5, 6]
        })

    @staticmethod
    def generate_range(n: int) -> List[Tuple[int, int]]:
        """
        Generates a list of squares for a given range.

        Args:
            n (int): The upper limit of the range.

        Returns:
            List[Tuple[int, int]]: A list of tuples containing the numbers and their squares.
        """
        return [(i, i ** 2) for i in range(n)]

    @staticmethod
    def exception_handling_demo() -> str:
        """
        Demonstrates exception handling.

        Returns:
            str: A message indicating whether an exception was raised.
        """
        try:
            # Simulate an exception (in a real application, use a library like requests)
            raise Exception("Test exception")
        except Exception:
            return "An exception was raised"

def main():
    print(StringUtils.say_hello("Python 3.12 User"))

    title = MathUtils.fetch_website_title("https://www.example.com")
    print(f"Website Title: {title}")

    mean_val = MathUtils.calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = MathUtils.create_dataframe()
    print("DataFrame:\n", df)

    text = "Python is fun and Python is powerful"
    word_count = StringUtils.count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Generated Range Squares:", MathUtils.generate_range(5))

    print("StringIO Buffer Output:\n" + StringUtils.string_io_example())

    print("Dictionary Iteration Output:")
    for line in StringUtils.dictionary_iteration():
        print(line)

    print("Exception Handling Test:", MathUtils.exception_handling_demo())

if __name__ == '__main__':
    main()