import string
import math
import pandas as pd
from typing import Dict, List, Tuple
from io import StringIO
from dataclasses import dataclass

@dataclass
class WebsiteTitle:
    title: str

@dataclass
class WordCount:
    word: str
    count: int

class StringUtils:
    @staticmethod
    def say_hello(name: str) -> str:
        """
        Returns a greeting message with the provided name.

        Args:
            name (str): The name to include in the greeting.

        Returns:
            str: A greeting message with the provided name.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """
        Counts the occurrences of each word in the provided text.

        Args:
            text (str): The text to count words from.

        Returns:
            Dict[str, int]: A dictionary where keys are words and values are their counts.
        """
        words = text.split()
        word_count = {}
        for word in words:
            word = word.strip(string.punctuation)
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        return word_count

    @staticmethod
    def string_io_example() -> str:
        """
        Returns a string generated from a StringIO buffer.

        Returns:
            str: A string generated from a StringIO buffer.
        """
        buffer = StringIO()
        buffer.write("Hello, World!")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """
        Returns a list of lines generated from a dictionary iteration.

        Returns:
            List[str]: A list of lines generated from a dictionary iteration.
        """
        dictionary = {"key1": "value1", "key2": "value2"}
        lines = []
        for key, value in dictionary.items():
            lines.append(f"{key}: {value}")
        return lines

class MathUtils:
    @staticmethod
    def fetch_website_title(url: str) -> str:
        """
        Fetches the title of a website from the provided URL.

        Args:
            url (str): The URL of the website.

        Returns:
            str: The title of the website.

        Raises:
            ValueError: If the URL is invalid.
        """
        # Simulate fetching the website title
        return "Example Website Title"

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """
        Calculates the mean of the provided numbers.

        Args:
            numbers (List[float]): The numbers to calculate the mean from.

        Returns:
            float: The mean of the numbers.

        Raises:
            ValueError: If the input list is empty.
        """
        if not numbers:
            raise ValueError("Input list is empty")
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """
        Creates a sample DataFrame.

        Returns:
            pd.DataFrame: A sample DataFrame.
        """
        data = {"Name": ["John", "Mary", "David"], "Age": [25, 31, 42]}
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """
        Generates a list of squares from 1 to n.

        Args:
            n (int): The upper limit.

        Returns:
            List[int]: A list of squares from 1 to n.
        """
        return [i ** 2 for i in range(1, n + 1)]

    @staticmethod
    def exception_handling_demo() -> str:
        """
        Demonstrates exception handling.

        Returns:
            str: A message indicating that the exception was handled.
        """
        try:
            # Simulate an exception
            raise ValueError("Test exception")
        except ValueError as e:
            return f"Exception handled: {e}"

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