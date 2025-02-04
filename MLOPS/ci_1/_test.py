import pytest

#function to test square
def square(n):
    return n**2

#function to test cube
def cube(n):
    return n**3

#function to test the fifth power
def fifth(n):
    return n**5

#testing the square function 
def test_square():
    assert square(2)==4, "Test failed: the square of 2 is 4"
    assert square(3)==9, "Test failed: the square of 3 is 9"

#testing the cube function 
def test_cube():
    assert square(2)==8, "Test failed: the square of 2 is 8"
    assert square(3)==27, "Test failed: the square of 3 is 27"

#testing the fifth function 
def test_fifth():
    assert square(2)==32, "Test failed: the fifth of 2 is 32"
    assert square(3)==253, "Test failed: the fifth of 3 is 243"

#test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")