from math_series import __version__
from math_series.series import *


def test_version():
    assert __version__ == '0.1.0'


"""Using unit tests for Test Driven Development as discussed in class"""

#base case fib with input 0
def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

#base case lucas with input 0
def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

#test case fib with small n 
def test_small_fib():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

# #test case lucas with small n 
def test_small_lucas():
    actual = lucas(3)
    expected = 3
    assert actual == expected

#test case fib with large n 
def test_lg_fib():
    actual = fibonacci(25)
    expected = 46368
    assert actual == expected


#test case lucas with large n 
def test_lg_lucas():
    actual = lucas(25)
    expected = 103682
    assert actual == expected
    
#test sum_series with (n,a,b)
def test_random():
    actual = sum_series(0,7,9)
    expected = 7
    assert actual == expected
    
# #test sum_series with (n,a,b)
def test_random():
    actual = sum_series(1,7,9)
    expected = 9
    assert actual == expected
    
# #test sum_series with (n,a,b)
def test_random():
    actual = sum_series(2,0,1)
    expected = 1
    assert actual == expected