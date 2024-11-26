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
        self.assertTrue(is_palindrome("racecar"))         
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))  
        self.assertTrue(is_palindrome("Able was I ere I saw Elba")) 
        self.assertTrue(is_palindrome("No x in Nixon"))  

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))           
        self.assertFalse(is_palindrome("Python"))          
        self.assertFalse(is_palindrome("abcdef"))          

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(" "))                 
        self.assertTrue(is_palindrome(""))                   
        self.assertTrue(is_palindrome("a"))      
if __name__ == '__main__':
    unittest.main()
