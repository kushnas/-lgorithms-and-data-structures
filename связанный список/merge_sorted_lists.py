import unittest
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    # Если один из списков пуст, возвращаем другой
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Указатели для обхода списков
    head = None
    
    # Устанавливаем начальную ссылку на меньший элемент
    if list1.value < list2.value:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    # Указатель для результата
    current = head  # Это будет указатель на последний добавленный узел

    # Объединяем списки путем изменения ссылок
    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next  # Двигаем указатель результата

    # Присоединяем оставшийся список, если есть
    if list1:
        current.next = list1
    else:
        current.next = list2

    return head  # Возвращаем новый объединенный список

def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=' -> ')
        current = current.next
    print('None')

class TestMergeSortedLists(unittest.TestCase):

    def test_merge_two_non_empty_lists(self):
        list1 = create_linked_list([3, 6, 8])
        list2 = create_linked_list([4, 7, 9, 11])
        merged_list = merge_sorted_lists(list1, list2)

        expected_result = [3, 4, 6, 7, 8, 9, 11]
        current = merged_list
        for value in expected_result:
            self.assertIsNotNone(current)
            self.assertEqual(current.value, value)
            current = current.next
        self.assertIsNone(current)

    def test_merge_first_list_empty(self):
        list1 = create_linked_list([])
        list2 = create_linked_list([1, 2, 3])
        merged_list = merge_sorted_lists(list1, list2)

        expected_result = [1, 2, 3]
        current = merged_list
        for value in expected_result:
            self.assertIsNotNone(current)
            self.assertEqual(current.value, value)
            current = current.next
        self.assertIsNone(current)

    def test_merge_second_list_empty(self):
        list1 = create_linked_list([1, 2, 3])
        list2 = create_linked_list([])
        merged_list = merge_sorted_lists(list1, list2)

        expected_result = [1, 2, 3]
        current = merged_list
        for value in expected_result:
            self.assertIsNotNone(current)
            self.assertEqual(current.value, value)
            current = current.next
        self.assertIsNone(current)

    def test_merge_two_empty_lists(self):
        list1 = create_linked_list([])
        list2 = create_linked_list([])
        merged_list = merge_sorted_lists(list1, list2)

        self.assertIsNone(merged_list)

    def test_merge_lists_with_same_elements(self):
        list1 = create_linked_list([1, 3, 5])
        list2 = create_linked_list([1, 3, 5])
        merged_list = merge_sorted_lists(list1, list2)

        expected_result = [1, 1, 3, 3, 5, 5]
        current = merged_list
        for value in expected_result:
            self.assertIsNotNone(current)
            self.assertEqual(current.value, value)
            current = current.next
        self.assertIsNone(current)

    def test_merge_lists_with_different_ranges(self):
        list1 = create_linked_list([10, 20, 30])

        list2 = create_linked_list([1, 2, 3])
        merged_list = merge_sorted_lists(list1, list2)

        expected_result = [1, 2, 3, 10, 20, 30]
        current = merged_list
        for value in expected_result:
            self.assertIsNotNone(current)
            self.assertEqual(current.value, value)
            current = current.next
        self.assertIsNone(current)

if __name__ == '__main__':
    # Запуск тестов
    unittest.main()