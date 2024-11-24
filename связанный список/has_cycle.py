import unittest

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

class TestHasCycle(unittest.TestCase):

    def test_empty_list(self):
        # Пустой список (нет узлов)
        self.assertFalse(has_cycle(None))

    def test_single_node_no_cycle(self):
        # Один узел без цикла
        node = ListNode(1)
        self.assertFalse(has_cycle(node))

    def test_single_node_with_cycle(self):
        # Один узел с циклом
        node = ListNode(1)
        node.next = node  # Создаем цикл
        self.assertTrue(has_cycle(node))

    def test_two_nodes_no_cycle(self):
        # Два узла без цикла
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        self.assertFalse(has_cycle(node1))

    def test_two_nodes_with_cycle(self):
        # Два узла с циклом
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1  # Создаем цикл
        self.assertTrue(has_cycle(node1))

    def test_multiple_nodes_with_cycle(self):
        # Множество узлов с циклом
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node1  # Создаем цикл
        self.assertTrue(has_cycle(node1))

    def test_multiple_nodes_no_cycle(self):
        # Множество узлов без цикла
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = None  # Нет цикла
        self.assertFalse(has_cycle(node1))

if __name__ == '__main__':
    unittest.main()