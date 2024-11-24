def shell_sort(arr):
    n = len(arr)
    gap = n // 2  
    
    while gap > 0:
        for current_position in range(gap, n):
            m_gap = current_position
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap
        gap //= 2 
    
    return arr

import unittest

class TestShellSort(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(shell_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])  
        self.assertEqual(shell_sort([3, 0, 2, 5, -1, 4, 1]), [-1, 0, 1, 2, 3, 4, 5])  
        self.assertEqual(shell_sort([1]), [1])  
        self.assertEqual(shell_sort([]), []) 

    def test_same_elements(self):
        self.assertEqual(shell_sort([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])  

    def test_reverse_sorted(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  

    def test_large_numbers(self):
        self.assertEqual(shell_sort([1000, 500, 1, 999, 300, 200]), [1, 200, 300, 500, 999, 1000])  

if __name__ == '__main__':
    unittest.main()