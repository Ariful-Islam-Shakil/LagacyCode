import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from your_module import your_function

@pytest.fixture
def mock_request():
    with patch('your_module.your_function') as mock:
        yield mock

def test_your_function(mock_request):
    mock_request.return_value = 'mocked_response'
    result = your_function()
    assert result == 'mocked_response'

def test_your_function_exception(mock_request):
    mock_request.side_effect = Exception('Mocked exception')
    with pytest.raises(Exception):
        your_function()

def test_your_function_property(mock_request):
    mock_request.return_value = MagicMock()
    mock_request.return_value.some_property = 'mocked_property'
    result = your_function()
    assert result.some_property == 'mocked_property'

def test_your_function_property_exception(mock_request):
    mock_request.side_effect = Exception('Mocked exception')
    with pytest.raises(Exception):
        your_function()

def test_your_function_property_getter(mock_request):
    mock_request.return_value = PropertyMock(side_effect=Exception('Mocked exception'))
    with pytest.raises(Exception):
        your_function().some_property