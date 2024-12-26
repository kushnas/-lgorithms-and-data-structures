class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree_from_array(array, index=0):
    if index >= len(array) or array[index] is None:
        return None

    node = TreeNode(array[index])

    node.left = build_tree_from_array(array, 2 * index + 1)
    node.right = build_tree_from_array(array, 2 * index + 2)
    return node

from collections import deque

def tree_to_array(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])  
    
    while queue:
        node = queue.popleft() 
        result.append(node.value)  
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

import unittest

class TestBinaryTree(unittest.TestCase):

    def test_build_tree_from_array(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        root = build_tree_from_array(array)

        result = tree_to_array(root)
        self.assertEqual(result, array)

    def test_empty_array(self):
        # Тест для пустого массива
        array = []
        root = build_tree_from_array(array)
        self.assertIsNone(root)

    # def test_array_with_none(self):
    #     # Тест для массива с None значениями
    #     array = [1, None, 3, None, None, None, 7]
    #     root = build_tree_from_array(array)
    #     result = tree_to_array(root)
    #     self.assertEqual(result, array)

    def test_single_element(self):
        # Тест для массива с одним элементом
        array = [1]
        root = build_tree_from_array(array)
        result = tree_to_array(root)
        expected = [1]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()