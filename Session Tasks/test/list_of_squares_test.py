import pytest
from scripts import squares 

def test_standard_input():
    result = squares.list_of_squares(3)
    assert result == {1: 1, 2: 4, 3: 9}
    assert len(result) == 3

def test_input_one():
    result = squares.list_of_squares(1)
    assert result == {1: 1}

def test_input_zero():
    assert squares.list_of_squares(0) == {}

def test_input_negative():
    # range(1, negative) is also empty.
    # Expect: Empty dictionary
    assert squares.list_of_squares(-5) == {}

def test_large_number():
    result = squares.list_of_squares(10)
    assert result[10] == 100  # 10 * 10
    assert result[5] == 25    # 5 * 5
    assert len(result) == 10

def test_invalid_type_float():
    with pytest.raises(TypeError):
        squares.list_of_squares(5.5)

def test_invalid_type_string():
    with pytest.raises(TypeError):
        squares.list_of_squares("5")