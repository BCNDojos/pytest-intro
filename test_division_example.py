import pytest
from division_example import divide

def test_something_right():
    assert divide(42, 1) == 42

def test_raises():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)