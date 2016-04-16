import pytest
from division_example import divide

@pytest.mark.parametrize("a", [1, 2, 3, 4])
def test_division_param(a):
    assert divide(a, 1) == a

@pytest.mark.parametrize("a", [(10, 2, 5), (100, 10, 10)])
def test_division_param_tuple(a):
    assert divide(a[0], a[1]) == a[2]