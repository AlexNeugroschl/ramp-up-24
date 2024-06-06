import pytest
from stuttering_function_easy import stutter

def test():
    assert stutter("word") == "wo... wo... word?"