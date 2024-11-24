import unittest


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item) 

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue") 
        return self.items.pop(0)  

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")  
        return self.items[0] 
    def get_size(self):
        return len(self.items) 

# Функция проверки является ли строка "a" подпоследовательностью строки "b"
def is_subsequence(a, b):
    q = Queue()
    
    # Добавляем все элементы строки a в очередь
    for el in a:
        q.enqueue(el)

    # Проходим по элементам строки b
    for el in b:
        if not q.is_empty() and q.peek() == el:
            q.dequeue()  # Удаляем элемент из очереди

    # Если очередь пуста, значит все элементы a найдены в b
    return q.get_size() == 0

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