def extra_letter(a, b):
    hash_map_b = {}
    
  
    for char in b:
        hash_map_b[char] = hash_map_b.get(char, 0) + 1
        
 
    for char in a:
        if char in hash_map_b:
            hash_map_b[char] -= 1
        

    for char, count in hash_map_b.items():
        if count == 1:
            return char
            
    return ""  
import unittest

class TestExtraLetter(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(extra_letter("abcd", "abcde"), "e")  
        self.assertEqual(extra_letter("abc", "abcd"), "d")    
        self.assertEqual(extra_letter("a", "aa"), "a")        
        self.assertEqual(extra_letter("xyz", "zyxq"), "q")     

    def test_empty_string(self):
        self.assertEqual(extra_letter("", "a"), "a")  
        self.assertEqual(extra_letter("", ""), "")      

    def test_same_characters(self):
        self.assertEqual(extra_letter("aabbccorekrtbotnhotynjyhjnyjiykhnj56jyjo65ny", "aabbccorekrtbotnhotynjyhjnyjiykhnj56jyjo65nyx"), "x") 
        self.assertEqual(extra_letter("xyz", "xyzy"), "y")      
if __name__ == '__main__':
    unittest.main()