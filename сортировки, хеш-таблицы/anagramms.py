def group_anagrams(strs):
    anagrams = {} 
    for s in strs:
        key = ''.join(sorted(s))
        
        if key not in anagrams:
            anagrams[key] = []
        
        anagrams[key].append(s)  
    return list(anagrams.values())

import unittest

class TestGroupAnagrams(unittest.TestCase):

    def test_anagrams(self):
        # Тест 1: Анагра́ммы с общими буквами
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertIn(sorted(["eat", "tea", "ate"]), [sorted(group) for group in result])
        self.assertIn(sorted(["tan", "nat"]), [sorted(group) for group in result])
        self.assertIn(sorted(["bat"]), [sorted(group) for group in result])
        
        # Тест 2: Другие слова
        result = group_anagrams(["won", "now", "aaa", "ooo", "ooo"])
        self.assertIn(sorted(["won", "now"]), [sorted(group) for group in result])
        self.assertIn(sorted(["aaa"]), [sorted(group) for group in result])
        self.assertIn(sorted(["ooo", "ooo"]), [sorted(group) for group in result])

    def test_empty_input(self):
        
        self.assertEqual(group_anagrams([]), [])  

    def test_single_string(self):
        
        self.assertEqual(group_anagrams(["test"]), [["test"]])  

    def test_no_anagrams(self):
       
        self.assertEqual(group_anagrams(["abc", "def", "ghi"]), [["abc"], ["def"], ["ghi"]])  

    def test_mixed_case_anagrams(self):
       
        result = group_anagrams(["aBc", "cAb", "CAB", "abc"])
        self.assertEqual(result,[["aBc"], ["cAb"], ["CAB"], ["abc"]])

if __name__ == '__main__':
    unittest.main()