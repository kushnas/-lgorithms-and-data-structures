# Сегодня утром жюри решило добавить в вариант олимпиады еще одну “Очень
# Легкую Задачу”. Ответственный секретарь Оргкомитета напечатал ее условие в
# одном экземпляре, и теперь ему нужно до начала олимпиады успеть сделать
# еще N копий. В его распоряжении имеются два ксерокса, один из которых
# копирует лист за х секунд, а другой – за y. (Разрешается использовать как один
# ксерокс, так и оба одновременно. Можно копировать не только с оригинала, но
# и с копии.) Помогите ему выяснить, какое минимальное время для этого
# потребуется.




def copy_time(n, x, y):
    left = 0
    right = (n - 1) * max(x, y)
    
    while left + 1 < right:
        middle = (right + left) // 2  # Используем целочисленное деление
        if middle // x + middle // y < n - 1:
            left = middle
        else:
            right = middle
    
    return right + min(x, y)


import unittest

class TestCopyTime(unittest.TestCase):

    def test_basic_cases(self):
        
        self.assertEqual(copy_time(2, 1, 1), 2)    
        self.assertEqual(copy_time(3, 2, 3), 4)    
        self.assertEqual(copy_time(4, 2, 2), 6)    
    
    def test_edge_cases(self):
       
        self.assertEqual(copy_time(3, 1, 2), 3)    
        self.assertEqual(copy_time(2, 1, 3), 2)    
        
        
        self.assertEqual(copy_time(5, 100, 100), 300)  
        self.assertEqual(copy_time(1, 1, 1), 1) 
    unittest.main()