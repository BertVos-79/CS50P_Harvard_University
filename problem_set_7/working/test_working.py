import pytest
from working import convert


def test_valid_cases():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("1:30 PM to 3:45 AM") == "13:30 to 03:45"

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 PM to 1 AM") == "13:00 to 01:00"


def test_invalid_cases():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 14:00 AM")
    with pytest.raises(ValueError):
        convert("12:30 PM to 12:60 AM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM till 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # 24-hour format not allowed


def test_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
