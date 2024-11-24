import unittest

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

class TestReverseArray(unittest.TestCase):
    
    def test_regular_case(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
    
    def test_empty_array(self):
        self.assertEqual(reverse_array([]), [])
    
    def test_single_element(self):
        self.assertEqual(reverse_array([42]), [42])
    
    def test_two_elements(self):
        self.assertEqual(reverse_array([1, 2]), [2, 1])
      
    def test_palindrome(self):
        self.assertEqual(reverse_array([1, 2, 1]), [1, 2, 1])
    
    def test_negative_numbers(self):
        self.assertEqual(reverse_array([-1, -2, -3]), [-3, -2, -1])
    
    def test_mixed_types(self):
        self.assertEqual(reverse_array([1, 'two', 3.0]), [3.0, 'two', 1])

if __name__ == '__main__':
    unittest.main()
