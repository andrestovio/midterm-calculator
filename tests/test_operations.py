import pytest
from app.operations import Addition, Subtraction, Multiplication, Division

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (1.5, 2.5, 4),
    (-1, -2, -3),
    (-1, 2, 1)
])
def test_addition(a, b, expected):
    assert Addition(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (5.5, 2.5, 3),
    (-1, -2, 1),
    (-1, 2, -3)
])
def test_subtraction(a, b, expected):
    assert Subtraction(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (1.5, 2, 3),
    (-1, -2, 2),
    (-1, 2, -2)
])
def test_multiplication(a, b, expected):
    assert Multiplication(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (5, 2, 2.5),
    (-6, -3, 2),
    (-6, 3, -2)
])
def test_division(a, b, expected):
    assert Division(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (1, 0),
    (0, 0),
    (-1, 0),
])
def test_division_by_zero(a, b):
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Division(a, b)
