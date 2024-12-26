from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree_from_array(array, index=0):
    """Строит бинарное дерево из массива."""
    if index >= len(array) or array[index] is None:
        return None

    node = TreeNode(array[index])
    node.left = build_tree_from_array(array, 2 * index + 1)
    node.right = build_tree_from_array(array, 2 * index + 2)
    return node

def is_symmetric(root):
    """Проверяет, является ли бинарное дерево симметричным."""
    if not root:
        return True

    queue = deque([(root.left, root.right)])

    while queue:
        left, right = queue.popleft()
  
        if not left and not right:
            continue

        if not left or not right:
            return False
        
        if left.value != right.value:
            return False
        
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))


    return True

import unittest
class TestIsSymmetric(unittest.TestCase):
    def test_symmetric_tree(self):
        self.assertTrue(is_symmetric(build_tree_from_array([1, 2, 2, 3, 4, 4, 3, 5, 5,5,5,5,5,5,5])))
        self.assertFalse(is_symmetric(build_tree_from_array([1, 2, 2, None, 3, None, 3])))


if __name__ == "__main__":
    unittest.main()
