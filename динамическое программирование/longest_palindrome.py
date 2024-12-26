def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    longest = s[0]  # Начальная палиндромная строка
    
    # Проверяем все подстроки длиной 2 и более
    for length in range(1, n +1):  # Длина подстроки от 2 до n
        for i in range(n - length +1):  # Левая граница подстроки
            substring = s[i:i + length]  # Получаем подстроку
            
            if is_palindrome(substring):  # Проверяем, является ли подстрока палиндромом
                if length > len(longest):  # Если длина больше, обновляем longest
                    longest = substring
    
    return longest

import unittest

class TestLongestPalindrome(unittest.TestCase):

    def test_example_cases(self):
        self.assertEqual(longest_palindrome("babad"), "bab")  # или "aba"
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        self.assertEqual(longest_palindrome("a"), "a")  # Односимвольная строка
        self.assertEqual(longest_palindrome("ac"), "a")  # Или "c", так как оба являются палиндромами

    def test_empty_string(self):
        self.assertEqual(longest_palindrome(""), "")  # Пустая строка

    def test_single_character_repeated(self):
        self.assertEqual(longest_palindrome("aaaaa"), "aaaaa")  # Полностью палиндромная строка

    def test_non_palindrome(self):
        self.assertEqual(longest_palindrome("abcde"), "a")  # Первый символ, так как все длиной 1 являются палиндромами

    def test_palindrome_at_the_end(self):
        self.assertEqual(longest_palindrome("abcdeedcba"), "abcdeedcba")  # Полная палиндромная строка

    def test_palindrome_in_middle(self):
        self.assertEqual(longest_palindrome("abcbad"), "abcba")  

if __name__ == "__main__":
    unittest.main()