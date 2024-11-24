import unittest

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

class TestFindMiddleNode(unittest.TestCase):

    def setUp(self):
        self.ListNode1 = ListNode(1)
        self.ListNode2 = ListNode(2)
        self.ListNode3 = ListNode(3)
        self.ListNode1.next = self.ListNode2
        self.ListNode2.next = self.ListNode3
        
    def test_find_middle_node(self):
        middle_node = find_middle_node(self.ListNode1)
        self.assertEqual(middle_node.value, 2)

    def test_find_middle_node_single(self):
        single_ListNode = ListNode(42)
        node = find_middle_node(single_ListNode)
        self.assertEqual(node.value, 42)
        self.assertIsNone(node.next)

    def test_reverse_empty_list(self):
        empty_node = find_middle_node(None)
        self.assertIsNone(empty_node)

if __name__ == '__main__':
    unittest.main()    

