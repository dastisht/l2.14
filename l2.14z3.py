
def calculate_rectangle_area(length, width):
    """
    Функция для вычисления площади прямоугольника.

    >>> calculate_rectangle_area(5, 3)
    15.0
    >>> calculate_rectangle_area(-2, 4)
    Traceback (most recent call last):
    ...
    NegativeRectangleSizeError: Отрицательные размеры прямоугольника недопустимы
    >>> calculate_rectangle_area(7, -1)
    Traceback (most recent call last):
    ...
    NegativeRectangleSizeError: Отрицательные размеры прямоугольника недопустимы
    """
    if length < 0 or width < 0:
        raise NegativeRectangleSizeError()
    return length * width

if __name__ == "__main__":
    import doctest
    doctest.testmod()


class TestCalculateRectangleArea(unittest.TestCase):
    def test_positive_dimensions(self):
        self.assertEqual(calculate_rectangle_area(5, 3), 15.0)

    def test_negative_length(self):
        with self.assertRaises(NegativeRectangleSizeError):
            calculate_rectangle_area(-2, 4)

    def test_negative_width(self):
        with self.assertRaises(NegativeRectangleSizeError):
            calculate_rectangle_area(7, -1)

if __name__ == "__main__":
    unittest.main()

def test_positive_dimensions():
    assert calculate_rectangle_area(5, 3) == 15.0

def test_negative_length():
    with pytest.raises(NegativeRectangleSizeError):
        calculate_rectangle_area(-2, 4)

def test_negative_width():
    with pytest.raises(NegativeRectangleSizeError):
        calculate_rectangle_area(7, -1)
