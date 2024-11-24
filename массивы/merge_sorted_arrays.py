import unittest

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


if __name__ == '__main__':
    unittest.main()