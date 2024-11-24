import unittest

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_elements(head, val_to_find):
    # Создаем "dummy" узел
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    cur = head
    
    while cur is not None:
        if cur.value == val_to_find :
            prev.next = cur.next  # Убираем текущий узел
        else:
            prev = cur  # Двигаем prev вперед
        cur = cur.next  # Двигаем cur вперед

    return dummy.next  # Возвращаем новую голову без "dummy"


class TestRemoveElements(unittest.TestCase):

    def setUp(self):
        # Создание тестового связного списка: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None
        self.head = ListNode(1)
        self.head.next = ListNode(2)
        self.head.next.next = ListNode(6)
        self.head.next.next.next = ListNode(3)
        self.head.next.next.next.next = ListNode(4)
        self.head.next.next.next.next.next = ListNode(5)
        self.head.next.next.next.next.next.next = ListNode(6)

    def test_remove_multiple_elements(self):
        new_head = remove_elements(self.head, 6)
        
        # Проверяем, что 6 ушло из списка
        current = new_head
        while current is not None:
            self.assertNotEqual(current.value, 6)
            current = current.next

    def test_remove_head_element(self):
        # Удаляем элемент 1 (голова списка)
        new_head = remove_elements(self.head, 1)
        
        # Проверяем, что новая голова списка = 2
        self.assertEqual(new_head.value, 2)

    def test_remove_non_existent_element(self):
        # Удаляем элемент, отсутствующий в списке
        new_head = remove_elements(self.head, 99)
        
        # Новый список должен быть таким же, как и исходный
        current = self.head
        index = 0
        while current is not None:
            self.assertEqual(current.value, new_head.value)
            current = current.next
            new_head = new_head.next
            index += 1

    def test_empty_list(self):
        # Удаляем элемент из пустого списка
        new_head = remove_elements(None, 1)
        
        # Новый список должен быть None
        self.assertIsNone(new_head)

    def test_remove_all_elements(self):
        # Создаем связный список из одинаковых элементов
        head_all_same = ListNode(7)
        head_all_same.next = ListNode(7)
        head_all_same.next.next = ListNode(7)

        new_head = remove_elements(head_all_same, 7)

        # Проверяем, что вернулся None
        self.assertIsNone(new_head)

if __name__ == '__main__':
    unittest.main()