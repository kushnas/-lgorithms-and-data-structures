import unittest

def even_first(arr):
    even_index = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1
    return arr


class TestEvenFirstFunction(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(even_first([3, 2, 4, 1, 11, 8, 9]), [2, 4, 8, 1, 11, 3, 9])

    def test_all_even(self):
        self.assertEqual(even_first([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_all_odd(self):
        self.assertEqual(even_first([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_empty_array(self):
        self.assertEqual(even_first([]), [])

    def test_single_element_even(self):
        self.assertEqual(even_first([2]), [2])

    def test_single_element_odd(self):
        self.assertEqual(even_first([1]), [1])

    def test_with_negatives(self):
        self.assertEqual(even_first([-1, -2, -3, -4]), [-2, -4, -3, -1])


if __name__ == '__main__':
    unittest.main()