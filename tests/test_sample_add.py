import pytest
from sample_add import add_spl

def test_add_spl_basic():
    assert add_spl(1, 2) == 4   # 1 + 2 + 1 = 4

def test_add_spl_negative():
    assert add_spl(-1, 5) == 5  # -1 + 5 + 1 = 5

def test_add_spl_zero():
    assert add_spl(0, 0) == 1   # 0 + 0 + 1 = 1
