class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def get_size(self):
        return len(self.items)
    


def is_palindrome(s):
    stack = Stack()
    
    # Игнорируем пробелы и приводим к нижнему регистру
    s = s.replace(" " , "").lower()
    
    for char in s:
        stack.push(char)

    for char in s:
        if char != stack.pop():
            return False
            
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