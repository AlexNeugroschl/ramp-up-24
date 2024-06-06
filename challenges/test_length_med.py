import pytest 
from length_of_number_medium import number_length

def test():
    assert number_length(5000) == 4
    assert number_length(50) == 2
    assert number_length(5) == 1
    assert number_length(500000) == 6
    assert number_length(5000000000) == 10