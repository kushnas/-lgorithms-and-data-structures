import unittest


def is_subsequence(a,b):
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            i+=1
        j+=1
    return i==len(a)


class TestIsSubsequence(unittest.TestCase):

    def test_positive_cases(self):
        self.assertTrue(is_subsequence('abc', 'ahbgdc'))  

    def test_negative_cases(self):
        self.assertFalse(is_subsequence('axc', 'ahbgdc'))  
        self.assertFalse(is_subsequence('abcd', 'ab'))      
        self.assertFalse(is_subsequence('abc', 'gotcha'))   
    
    def test_edge_cases(self):
        self.assertTrue(is_subsequence('', ''))               
        self.assertFalse(is_subsequence('a', ''))            
        self.assertFalse(is_subsequence('abcd', ''))        

if __name__ == '__main__':
    unittest.main()