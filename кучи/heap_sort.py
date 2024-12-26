import unittest
from max_heap_sift_down import sift_down
def heap_sort(arr):
    n = len(arr)

    # Строим максимальную кучу
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

    # Извлекаем элементы из кучи один за другим
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Перемещаем текущий корень в конец
        sift_down(arr, 0, i)  # Восстанавливаем свойства кучи на уменьшенном массиве

class TestHeapSort(unittest.TestCase):
    
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        heap_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_empty_array(self):
        arr = []
        heap_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [42]
        heap_sort(arr)
        self.assertEqual(arr, [42])

    def test_float_array(self):
        arr = [3.1, 2.2, 5.5, 4.4]
        heap_sort(arr)
        self.assertEqual(arr, [2.2, 3.1, 4.4, 5.5])

    def test_negative_numbers(self):
        arr = [-1, -3, -2, 0, 2]
        heap_sort(arr)
        self.assertEqual(arr, [-3, -2, -1, 0, 2])

if __name__ == "__main__":
    unittest.main()