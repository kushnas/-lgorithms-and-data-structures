def length_of_lis(nums):
    if not nums:
        return 0
    
    if len(nums)==1:
        return 1

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        if nums[i-1]<nums[i]:
            dp[i]=dp[i-1]+1
        return max(dp)  

import unittest

class TestLengthOfLIS(unittest.TestCase):

    def test_increasing_sequence(self):
        self.assertEqual(length_of_lis([1, 2, 3, 4, 5]), 5) 
        self.assertEqual(length_of_lis([3, 5, 6, 7, 8]), 5) 
        self.assertEqual(length_of_lis([1, 1, 1, 1]), 1)  

    def test_mixed_sequence(self):
        self.assertEqual(length_of_lis([3, 2, 8, 9, 5, 10]), 3)  
        self.assertEqual(length_of_lis([1, 2, 7, 9, 0, 10]), 4)  
        self.assertEqual(length_of_lis([4, 3, 2, 1, 0]), 1)  


    def test_single_element_array(self):
        self.assertEqual(length_of_lis([10]), 1)  

    def test_repeating_elements(self):
        self.assertEqual(length_of_lis([5, 1, 5, 2, 3, 4]), 3)  
        self.assertEqual(length_of_lis([8, 8, 8, 8]), 1)  

if __name__ == "__main__":
    unittest.main()