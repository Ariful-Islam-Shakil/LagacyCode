import string
import typing
from dataclasses import dataclass
from typing import Dict, List, Tuple
import pandas as pd
from io import StringIO
import math

class StringUtils:
    """String utility class."""
    
    @staticmethod
    def say_hello(name: str) -> str:
        """Print a greeting message.

        Args:
            name (str): The name to greet.

        Returns:
            str: The greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """Count the occurrences of each word in a given text.

        Args:
            text (str): The text to count words from.

        Returns:
            Dict[str, int]: A dictionary with words as keys and their counts as values.
        """
        words = text.split()
        word_count = {}
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    @staticmethod
    def string_io_example() -> str:
        """Example usage of StringIO.

        Returns:
            str: The output of the StringIO example.
        """
        buffer = StringIO()
        buffer.write("Hello, World!\n")
        buffer.write("This is a test.\n")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """Iterate over a dictionary.

        Returns:
            List[str]: A list of dictionary keys.
        """
        dictionary = {"key1": "value1", "key2": "value2"}
        return list(dictionary.keys())

class MathUtils:
    """Math utility class."""
    
    @staticmethod
    def fetch_website_title(url: str) -> str:
        """Fetch the title of a website.

        Args:
            url (str): The URL of the website.

        Returns:
            str: The title of the website.
        """
        # Simulate fetching the website title
        return "Example Website Title"

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """Calculate the mean of a list of numbers.

        Args:
            numbers (List[float]): The list of numbers.

        Returns:
            float: The mean of the numbers.
        """
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """Create a sample DataFrame.

        Returns:
            pd.DataFrame: The sample DataFrame.
        """
        data = {"Name": ["John", "Mary", "David"], "Age": [25, 31, 42]}
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """Generate a range of numbers.

        Args:
            n (int): The number of numbers to generate.

        Returns:
            List[int]: The generated range of numbers.
        """
        return list(range(n))

    @staticmethod
    def exception_handling_demo() -> str:
        """Demonstrate exception handling.

        Returns:
            str: The result of the exception handling demo.
        """
        try:
            # Simulate an exception
            raise Exception("Test exception")
        except Exception as e:
            return f"Caught exception: {str(e)}"

def main() -> None:
    """The main function."""
    
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