

def is_palindrome(s):
    s = s.replace(" " , "").lower()
    left = 0
    right = len(s) - 1
    while (left < right) :
        if (s[left] != s[right]):
            return False
        left+=1
        right-=1
    return True

import unittest

class TestIsPalindrome(unittest.TestCase):

    def test_palindromes(self):
        self.assertTrue(is_palindrome("racecar"))         # Ожидается True
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))  # Ожидается True
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))  # Ожидается True
        self.assertTrue(is_palindrome("No x in Nixon"))  # Ожидается True

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))           # Ожидается False
        self.assertFalse(is_palindrome("Python"))          # Ожидается False
        self.assertFalse(is_palindrome("abcdef"))          # Ожидается False

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(" "))                 # Пустая строка считается палиндромом
        self.assertTrue(is_palindrome(""))                   # Пустая строка
        self.assertTrue(is_palindrome("a"))                  # Одна буква считается палиндромом

if __name__ == '__main__':
    unittest.main()
