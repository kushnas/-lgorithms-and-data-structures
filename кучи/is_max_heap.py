import unittest


def is_max_heap(arr):
    """Проверяет, является ли массив максимальной кучей."""
    n = len(arr)
    for i in range((n-1)//2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False  # Родитель меньше левого потомка
        if right < n and arr[i] < arr[right]:
            return False  # Родитель меньше правого потомка
    return True

class TestMaxHeap(unittest.TestCase):

    def test_valid_max_heap(self):
        self.assertTrue(is_max_heap([10, 9, 8, 7, 6, 5, 4]))
        self.assertTrue(is_max_heap([100, 50, 30, 20, 10, 5]))
        self.assertTrue(is_max_heap([30, 20, 15, 10, 8, 5, 3, 1]))

    def test_invalid_max_heap(self):
        self.assertFalse(is_max_heap([10, 20, 30]))
        self.assertFalse(is_max_heap([3, 1, 4, 2, 5]))
        self.assertFalse(is_max_heap([10, 5, 20, 15]))

    def test_empty_heap(self):
        self.assertTrue(is_max_heap([]))  

    def test_single_element_heap(self):
        self.assertTrue(is_max_heap([42]))  

    def test_duplicate_elements_heap(self):
        self.assertTrue(is_max_heap([5, 5, 5, 5])) 

    def test_valid_heap_with_negative_numbers(self):
        self.assertTrue(is_max_heap([-1, -2, -3, -4]))  

if __name__ == "__main__":
    unittest.main()