def binary_search_sqrt(target):
    if target < 0:
        raise ValueError("Cannot compute square root of a negative number")
    
    l, r = 0, target
    
    while l <= r:
        middle = (l + r) // 2 
        middle_squared = middle * middle
        
        if middle_squared > target:
            r = middle - 1
        elif middle_squared < target:
            l = middle + 1
        else:
            return middle  # Найден точный корень
    
    return r  # Возвращаем ближайший целый корень числа

import unittest

class TestBinarySearchSqrt(unittest.TestCase):

    def test_perfect_squares(self):
        self.assertEqual(binary_search_sqrt(0), 0)   # Корень 0
        self.assertEqual(binary_search_sqrt(1), 1)   # Корень 1
        self.assertEqual(binary_search_sqrt(4), 2)   # Корень 4
        self.assertEqual(binary_search_sqrt(9), 3)   # Корень 9
        self.assertEqual(binary_search_sqrt(16), 4)  # Корень 16
        self.assertEqual(binary_search_sqrt(25), 5)  # Корень 25

    def test_non_perfect_squares(self):
        self.assertEqual(binary_search_sqrt(3), 1)   # Ближайший корень 1
        self.assertEqual(binary_search_sqrt(5), 2)   # Ближайший корень 2
        self.assertEqual(binary_search_sqrt(10), 3)  # Ближайший корень 3
        self.assertEqual(binary_search_sqrt(15), 3)  # Ближайший корень 3
        self.assertEqual(binary_search_sqrt(20), 4)  # Ближайший корень 4
        self.assertEqual(binary_search_sqrt(30), 5)  # Ближайший корень 5

    def test_edge_cases(self):
        self.assertEqual(binary_search_sqrt(2), 1)   # Ближайший корень 1
        self.assertEqual(binary_search_sqrt(8), 2)   # Ближайший корень 2
        self.assertEqual(binary_search_sqrt(7), 2)   # Ближайший корень 2

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            binary_search_sqrt(-1)  # Ожидаем исключение для отрицательных чисел

if __name__ == '__main__':
    unittest.main()