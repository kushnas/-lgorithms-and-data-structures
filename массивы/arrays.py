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




def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Если в каком-то из массивов остались элементы, добавляем их в конец слияния
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])

    return merged_array


class TestMergeSortedArrays(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_sorted_arrays([], [4, 5, 6]), [4, 5, 6])
        self.assertEqual(merge_sorted_arrays([], []), [])
        self.assertEqual(merge_sorted_arrays([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sorted_arrays([5, 6], [1, 2, 3]), [1, 2, 3, 5, 6])
        self.assertEqual(merge_sorted_arrays([1], [2]), [1, 2])
        self.assertEqual(merge_sorted_arrays([2], [1]), [1, 2])



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

def even_first(arr):
    even_index = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1
    return arr

import unittest

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
