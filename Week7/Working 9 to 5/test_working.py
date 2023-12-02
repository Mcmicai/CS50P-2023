from working import convert
import pytest


def test_convert():
    with pytest.raises(ValueError):
        convert("12:60 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("12:60 PM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("14:00 PM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("14:00 PM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM - 14:00 PM")
    with pytest.raises(ValueError):
        convert("1 AM - 1 PM")

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"