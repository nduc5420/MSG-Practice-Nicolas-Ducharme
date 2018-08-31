"""Tests the mathematical functions defined in my_pkg/trail.py
"""

import pytest

def test_square():
    """Tests the squaring function"""

    from python_package.trial import square

    assert 4 == square(2)

def test_factorial():
    "Tests the factorial function"

    from python_package.trial import factorial

    assert 24 == factorial(4)
    assert 6 == factorial(3.0)
    assert 1 == factorial(0)
    assert 1 == factorial(-1)

    with pytest.raises(ValueError):
        factorial(3.5)

def test_add_all_ints():
    "Test the sum function"

    from python_package.trial import add_all_ints

    assert 55 == add_all_ints(10)
    assert 0 == add_all_ints(0)
    assert 1 == add_all_ints(1)
    assert 3 == add_all_ints(2.0)

    with pytest.raises(ValueError):
        add_all_ints(3.2)
        add_all_ints(-1)
  
    
    
