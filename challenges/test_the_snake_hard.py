import pytest
from the_snake_area_filling_hard import snakefill

def test():
    assert snakefill(3) == 3
    assert snakefill(6) == 5
    assert snakefill(24) == 9