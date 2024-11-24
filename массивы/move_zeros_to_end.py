import unittest

def move_zeros_to_end(arr):

    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

class TestMoveZerosToEnd(unittest.TestCase):

    def test_example_cases(self):
        example1 = [0, 0, 1, 0, 3, 12]
        move_zeros_to_end(example1)
        self.assertEqual(example1, [1, 3, 12, 0, 0, 0])

        example2 = [0, 33, 57, 88, 60, 0, 0, 80, 99]
        move_zeros_to_end(example2)
        self.assertEqual(example2, [33, 57, 88, 60, 80, 99, 0, 0, 0])

        example3 = [0, 0, 0, 18, 16, 0, 0, 77, 99]
        move_zeros_to_end(example3)
        self.assertEqual(example3, [18, 16, 77, 99, 0, 0, 0, 0, 0])

    def test_no_zeros(self):
        arr = [1, 2, 3, 4, 5]
        move_zeros_to_end(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5]) 
    def test_only_zeros(self):
        arr = [0, 0, 0, 0]
        move_zeros_to_end(arr)
        self.assertEqual(arr, [0, 0, 0, 0])  

    def test_alternating_zeros(self):
        arr = [0, 1, 0, 2, 0, 3]
        move_zeros_to_end(arr)
        self.assertEqual(arr, [1, 2, 3, 0, 0, 0])  

    def test_single_element(self):
        arr = [0]
        move_zeros_to_end(arr)
        self.assertEqual(arr, [0])  

        arr = [1]
        move_zeros_to_end(arr)
        self.assertEqual(arr, [1])  

if __name__ == '__main__':
    unittest.main()