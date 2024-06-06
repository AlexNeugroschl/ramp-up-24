import pytest
import imaginary_coding_interview_hard

def test():
    assert interview([5, 5, 10, 10, 15, 15, 20, 20], 120) == "qualified"
    assert interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ==  "qualified"
    assert interview([5, 5, 10, 10, 25, 15, 20, 20], 120) == "disqualified"