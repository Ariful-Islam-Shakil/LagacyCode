# pytest.ini
[pytest]
python_version = 3.12

# test_file.py
import pytest
from unittest.mock import patch
from your_module import your_function

@pytest.mark.parametrize("input_value, expected_output", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_your_function(input_value, expected_output):
    with patch('your_module.your_function') as mock_your_function:
        mock_your_function.return_value = expected_output
        result = your_function(input_value)
        assert result == expected_output

def test_your_function_invalid_input():
    with pytest.raises(ValueError):
        your_function('a')

def test_your_function_edge_case():
    with pytest.raises(TypeError):
        your_function(None)

def test_your_function_edge_case_2():
    with pytest.raises(TypeError):
        your_function(1.5)

def test_your_function_edge_case_3():
    with pytest.raises(TypeError):
        your_function('1.5')

def test_your_function_edge_case_4():
    with pytest.raises(TypeError):
        your_function(True)

def test_your_function_edge_case_5():
    with pytest.raises(TypeError):
        your_function(False)