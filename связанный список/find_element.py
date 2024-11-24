import unittest
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_element(head, target):
    current = head
    while current:
        if current.value == target:
            return current
        current = current.next
    return None


class TestFindElement(unittest.TestCase):

    def setUp(self):
        # Создание тестового связного списка: 1 -> 2 -> 3 -> 4 -> 5 -> None
        self.head = ListNode(1)
        self.head.next = ListNode(2)
        self.head.next.next = ListNode(3)
        self.head.next.next.next = ListNode(4)
        self.head.next.next.next.next = ListNode(5)

    def test_find_element_present(self):
        # Проверяем, что функция находит элемент 3
        result = find_element(self.head, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 3)

    def test_find_element_not_present(self):
        # Проверяем, что функция не находит элемент, которого нет (например, 6)
        result = find_element(self.head, 6)
        self.assertIsNone(result)

    def test_find_head_element(self):
        # Проверяем, что функция находит голову списка (значение 1)
        result = find_element(self.head, 1)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 1)
        
    def test_find_last_element(self):
        # Проверяем, что функция находит последний элемент (значение 5)
        result = find_element(self.head, 5)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 5)

    def test_empty_list(self):
        # Проверяем, что функция возвращает None для пустого списка
        empty_head = None
        result = find_element(empty_head, 1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()