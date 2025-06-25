import typing
from dataclasses import dataclass
from typing import Dict, List
import requests
from unittest.mock import monkeypatch
from urllib.parse import urlparse

@dataclass
class WebsiteTitle:
    title: str

def calculate_mean(numbers: List[float]) -> float:
    """
    Calculate the mean of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The mean of the numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list is empty")
    return sum(numbers) / len(numbers)

def create_dataframe() -> Dict[str, List[float]]:
    """
    Create a sample dataframe with a 'score' column.

    Returns:
        A dictionary representing the dataframe.
    """
    return {'score': [1.0, 2.0, 3.0]}

def generate_range(n: int) -> List[int]:
    """
    Generate a list of numbers from 0 to n with a step of 1, and append n+1 to the list.

    Args:
        n: The upper limit of the range.

    Returns:
        A list of numbers.
    """
    return list(range(n + 1))

def exception_handling_demo() -> str:
    """
    Demonstrate exception handling.

    Returns:
        A message indicating that an error was caught.
    """
    try:
        raise Exception("Something went wrong")
    except Exception as e:
        return f"Caught an error: {str(e)}"

def fetch_website_title(url: str) -> WebsiteTitle:
    """
    Fetch the title of a website.

    Args:
        url: The URL of the website.

    Returns:
        A WebsiteTitle object containing the title of the website.

    Raises:
        requests.RequestException: If the request fails.
    """
    response = requests.get(url)
    response.raise_for_status()
    return WebsiteTitle(urlparse(response.url).path.split("/")[-1])

def test_calculate_mean() -> None:
    assert calculate_mean([1, 2, 3]) == 2.0

def test_create_dataframe() -> None:
    df = create_dataframe()
    assert 'score' in df
    assert len(df['score']) == 3

def test_generate_range() -> None:
    assert generate_range(3) == [0, 1, 2, 3]

def test_exception_handling_demo() -> None:
    assert "Caught an error" in exception_handling_demo()

def test_fetch_website_title(monkeypatch: monkeypatch) -> None:
    class MockResponse:
        text = "<html><head><title>Example</title></head></html>"
    def mock_get(url: str) -> MockResponse:
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)
    assert fetch_website_title("any").title == "Example"