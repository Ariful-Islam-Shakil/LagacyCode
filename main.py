import string
import math
import pandas as pd
from typing import Dict, List, Tuple

class MathUtils:
    """Utility class for mathematical operations."""

    @staticmethod
    def fetch_website_title(url: str) -> str:
        """Fetch the title of a website.

        Args:
            url (str): The URL of the website.

        Returns:
            str: The title of the website.

        Raises:
            ValueError: If the URL is invalid.
        """
        # Implement website title fetching logic here
        return "Example Website Title"

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """Calculate the mean of a list of numbers.

        Args:
            numbers (List[float]): The list of numbers.

        Returns:
            float: The mean of the numbers.

        Raises:
            ValueError: If the input list is empty.
        """
        if not numbers:
            raise ValueError("Input list cannot be empty")
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """Create a sample DataFrame.

        Returns:
            pd.DataFrame: The sample DataFrame.
        """
        data = {
            "Name": ["John", "Anna", "Peter"],
            "Age": [28, 24, 35]
        }
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """Generate a list of squares of numbers from 1 to n.

        Args:
            n (int): The upper limit.

        Returns:
            List[int]: The list of squares.
        """
        return [i ** 2 for i in range(1, n + 1)]

    @staticmethod
    def exception_handling_demo() -> str:
        """Demonstrate exception handling.

        Returns:
            str: A message indicating successful exception handling.
        """
        try:
            # Simulate an exception
            raise ValueError("Test exception")
        except ValueError as e:
            return f"Caught exception: {e}"
        else:
            return "No exception occurred"

class StringUtils:
    """Utility class for string operations."""

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
            text (str): The input text.

        Returns:
            Dict[str, int]: A dictionary with word counts.
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
        """Demonstrate StringIO usage.

        Returns:
            str: A sample StringIO output.
        """
        # Implement StringIO example logic here
        return "Sample StringIO Output"

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """Demonstrate dictionary iteration.

        Returns:
            List[str]: A list of dictionary keys.
        """
        data = {"key1": "value1", "key2": "value2"}
        return list(data.keys())

def main():
    """The main entry point of the program."""
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