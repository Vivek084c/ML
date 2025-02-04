import pytest

# Function to test square
def square(n):
    return n**2

# Function to test cube
def cube(n):
    return n**3

# Function to test the fifth power
def fifth(n):
    return n**5

# Testing the square function 
def test_square():
    assert square(2) == 4, "Test failed: the square of 2 is 4"
    assert square(3) == 9, "Test failed: the square of 3 is 9"

# Testing the cube function 
def test_cube():
    assert cube(2) == 8, "Test failed: the cube of 2 is 8"
    assert cube(3) == 27, "Test failed: the cube of 3 is 27"

# Testing the fifth function 
def test_fifth():
    assert fifth(2) == 32, "Test failed: the fifth of 2 is 32"
    assert fifth(3) == 243, "Test failed: the fifth of 3 is 243"

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")