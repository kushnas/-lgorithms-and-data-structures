import unittest

def merge_sorted_arrays(arr1, arr2):
    i, j, k = len(arr1) - len(arr2) - 1, len(arr2) - 1, len(arr1) - 1

    # Слияние массивов с конца
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    # Если остались элементы во втором массиве, копируем их
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

class TestMergeSortedArrays(unittest.TestCase):
    def test_merge_with_non_empty_arrays(self):
        arr1 = [1, 3, 5, 0, 0, 0]
        arr2 = [2, 4, 6]
        merge_sorted_arrays(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6])

    def test_merge_with_empty_second_array(self):
        arr1 = [1, 3, 5]
        arr2 = []
        merge_sorted_arrays(arr1, arr2)
        self.assertEqual(arr1, [1, 3, 5])

    def test_merge_with_empty_first_array(self):
        arr1 = [0, 0, 0]
        arr2 = [2, 4, 6]
        merge_sorted_arrays(arr1, arr2)
        self.assertEqual(arr1, [2, 4, 6])

    def test_merge_with_equal_elements(self):
        arr1 = [1, 2, 3, 0, 0, 0]
        arr2 = [1, 2, 3]
        merge_sorted_arrays(arr1, arr2)
        self.assertEqual(arr1, [1, 1, 2, 2, 3, 3])

    def test_merge_with_negative_numbers(self):
        arr1 = [-5, -3, -1, 0, 0, 0]
        arr2 = [-4, -2, -1]
        merge_sorted_arrays(arr1, arr2)
        self.assertEqual(arr1, [-5, -4, -3, -2, -1, -1])

    def test_merge_with_large_numbers(self):
        arr1 = [1000000, 2000000, 3000000, 0, 0]
        arr2 = [1500000, 2500000]
        merge_sorted_arrays(arr1, arr2)
        self.assertEqual(arr1, [1000000, 1500000, 2000000, 2500000, 3000000])


if __name__ == '__main__':
    unittest.main()