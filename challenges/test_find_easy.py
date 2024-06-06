import pytest
import find_the_discount_easy

def test_discount():
    assert  dis(100, 25) == 75
    assert  dis(100, 75) == 25
    assert  dis(100, 10) == 90
    assert  dis(100, 50) == 50
    assert  dis(30, 10) == 27