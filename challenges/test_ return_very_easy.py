import pytest
from return_the_sum_of_two_numbers_very_easy import addition

def test():
    assert addition(5,3) == 8
    assert addition(9,3) == 12
    assert addition(10,6) == 16
    assert addition(45,65) == 110