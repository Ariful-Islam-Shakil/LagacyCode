import pytest
from unittest.mock import patch
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

@patch('utils.math_utils.requests.get')
def test_fetch_website_title(mock_get):
    mock_response = "<html><head><title>Example</title></head></html>"
    mock_get.return_value.text = mock_response
    assert mu.fetch_website_title("any") == "Example"