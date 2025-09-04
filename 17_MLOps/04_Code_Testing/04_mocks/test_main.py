import pytest 
from main import get_weather

def test_get_weather(mocker):
    # Mock request.get
    mock_get = mocker.patch("main.requests.get")

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # Call function
    result = get_weather("Mumbai")

    # Assertions
    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Mumbai")