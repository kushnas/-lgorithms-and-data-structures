def feed_animals(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0
    
    animals.sort()  
    food.sort()     
    count = 0
    for f in food:
        if f >= animals[count]:  
            count += 1
        if count == len(animals):  
            break
            
    return count

import unittest

class TestFeedAnimals(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(feed_animals([1, 2, 3], [3, 2, 1]), 3)  
        self.assertEqual(feed_animals([1, 2], [1, 2, 3]), 2)     
        self.assertEqual(feed_animals([5, 3], [1, 2, 3]), 1)     

    def test_empty_input(self):
        self.assertEqual(feed_animals([], [1, 2, 3]), 0)  
        self.assertEqual(feed_animals([1, 2], []), 0)      
        self.assertEqual(feed_animals([], []), 0)          

    def test_exact_fit(self):
        self.assertEqual(feed_animals([1, 2, 3], [1, 2, 3]), 3)  
        self.assertEqual(feed_animals([3, 2, 1], [1, 2, 3]), 3)  
    
    def test_some_animals_fed(self):
        self.assertEqual(feed_animals([5, 4, 3], [3, 2, 5]), 2)  
        self.assertEqual(feed_animals([5, 4], [6, 1, 2, 3]), 1)  

if __name__ == '__main__':
    unittest.main()

