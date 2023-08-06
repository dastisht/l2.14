
def get_element(lst, index):
    """
    Функция для получения элемента списка по индексу.

    >>> get_element([1, 2, 3, 4, 5], 2)
    3
    >>> get_element([1, 2, 3, 4, 5], -1)
    Traceback (most recent call last):
    ...
    NegativeIndexError: Отрицательные индексы недопустимы
    >>> get_element([1, 2, 3, 4, 5], 10)
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    """
    if index < 0:
        raise NegativeIndexError()
    return lst[index]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

class TestGetElement(unittest.TestCase):
    def test_positive_index(self):
        self.assertEqual(get_element([1, 2, 3, 4, 5], 2), 3)

    def test_negative_index(self):
        with self.assertRaises(NegativeIndexError):
            get_element([1, 2, 3, 4, 5], -1)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_element([1, 2, 3, 4, 5], 10)

if __name__ == "__main__":
    unittest.main()

def test_positive_index():
    assert get_element([1, 2, 3, 4, 5], 2) == 3

def test_negative_index():
    with pytest.raises(NegativeIndexError):
        get_element([1, 2, 3, 4, 5], -1)

def test_out_of_range_index():
    with pytest.raises(IndexError):
        get_element([1, 2, 3, 4, 5], 10)
