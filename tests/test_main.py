from src.main import add, subtract

def test_add_function():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(1, 0) == 1

def test_subtract_function():
    assert subtract(1, 2) == -1
    assert subtract(1, -1) == 2
    assert subtract(1, 0) == 1
    assert subtract(10, 5) == 5