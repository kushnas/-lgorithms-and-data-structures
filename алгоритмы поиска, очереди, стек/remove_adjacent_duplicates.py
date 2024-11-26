def remove_adjacent_duplicates(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Удаляем предыдущий символ, если он совпадает с текущим
        else:
            stack.append(char)  # Добавляем текущий символ в стек

    return ''.join(stack)  # Преобразуем стек обратно в строку

import unittest

class TestRemoveAdjacentDuplicates(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(remove_adjacent_duplicates("cdffd"), "c")  
        self.assertEqual(remove_adjacent_duplicates("xyyx"), "")     
        self.assertEqual(remove_adjacent_duplicates("fqffqzzsd"), "fsd")  
        self.assertEqual(remove_adjacent_duplicates("aaabba"), "")  
        self.assertEqual(remove_adjacent_duplicates("abccba"), "")    

    def test_no_duplicates(self):
        self.assertEqual(remove_adjacent_duplicates("abcdefg"), "abcdefg")
        self.assertEqual(remove_adjacent_duplicates(""), "")  
        
    def test_all_duplicates(self):
        self.assertEqual(remove_adjacent_duplicates("aaaaaa"), "")  
        
    def test_mixed_cases(self):
        self.assertEqual(remove_adjacent_duplicates("aabbccddeeffgghhiijj"), "")  
        self.assertEqual(remove_adjacent_duplicates("abcdeedcba"), "")  

if __name__ == '__main__':
    unittest.main()