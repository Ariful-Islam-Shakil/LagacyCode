import pytest
from unittest.mock import MagicMock
import utils.math_utils as mu

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 2.0),
    ([4, 5, 6], 5.0),
])
def test_calculate_mean(numbers, expected):
    assert mu.calculate_mean(numbers) == expected

def test_create_dataframe():
    df = mu.create_dataframe()
    assert 'score' in df.columns
    assert len(df) == 3

def test_generate_range():
    assert mu.generate_range(3) == [0, 1, 4]

def test_exception_handling_demo():
    assert "Caught an error" in mu.exception_handling_demo()

@pytest.mark.parametrize("url, expected", [
    ("any", "Example"),
])
def test_fetch_website_title(url, expected, monkeypatch):
    class MockResponse:
        text = "<html><head><title>Example</title></head></html>"
    mock_get = MagicMock(return_value=MockResponse())
    monkeypatch.setattr(mu.requests, "get", mock_get)
    assert mu.fetch_website_title(url) == expected