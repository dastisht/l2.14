
def divide(a, b):
    """
    Функция для деления двух чисел.

    >>> divide(10, 2)
    5.0
    >>> divide(0, 5)
    0.0
    >>> divide(8, 0)
    Traceback (most recent call last):
    ...
    DivisionByZeroError: Деление на ноль недопустимо
    """
    if b == 0:
        raise DivisionByZeroError()
    return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
import unittest 

class TestDivision(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(0, 5), 0.0)

    def test_division_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            divide(8, 0)

if __name__ == "__main__":
    unittest.main()

def test_positive_numbers():
    assert divide(10, 2) == 5.0
    assert divide(0, 5) == 0.0

def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        divide(8, 0)
