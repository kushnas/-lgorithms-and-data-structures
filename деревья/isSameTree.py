
import unittest

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_same_tree(p, q):
    """Проверяет, являются ли два бинарных дерева одинаковыми."""

    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.value != q.value:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.value != q.value:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class TestIsSameTree(unittest.TestCase):

    def test_both_trees_empty(self):
        root1 = None
        root2 = None
        self.assertTrue(is_same_tree(root1, root2))

    def test_one_tree_empty(self):
        root1 = TreeNode(1)
        root2 = None
        self.assertFalse(is_same_tree(root1, root2))

    def test_identical_trees(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        self.assertTrue(is_same_tree(root1, root2))


    def test_different_values(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(4)  # Значение отличается
        self.assertFalse(is_same_tree(root1, root2))

if __name__ == "__main__":
    unittest.main()