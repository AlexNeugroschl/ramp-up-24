import pytest
from  convert_minutes_into_seconds_very_easy import convert

def test_convert_works():
    assert convert(1) == 60
    assert convert(10) == 600
    assert convert(5) == 300
    assert convert(2) == 120
