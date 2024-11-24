import unittest

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse_linked_list(head):
    prev_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node

class TestReverseLinkedList(unittest.TestCase):

    def setUp(self):
        self.ListNode1 = ListNode(1)
        self.ListNode2 = ListNode(2)
        self.ListNode3 = ListNode(3)
        self.ListNode1.next = self.ListNode2
        self.ListNode2.next = self.ListNode3
        
    def test_reverse_multiple_ListNodes(self):
        reversed_head = reverse_linked_list(self.ListNode1)
        self.assertEqual(reversed_head.data, 3)
        self.assertEqual(reversed_head.next.data, 2)
        self.assertEqual(reversed_head.next.next.data, 1)
        self.assertIsNone(reversed_head.next.next.next)

    def test_reverse_single_ListNode(self):
        single_ListNode = ListNode(42)
        reversed_head = reverse_linked_list(single_ListNode)
        self.assertEqual(reversed_head.data, 42)
        self.assertIsNone(reversed_head.next)

    def test_reverse_empty_list(self):
        reversed_head = reverse_linked_list(None)
        self.assertIsNone(reversed_head)

if __name__ == '__main__':
    unittest.main()    