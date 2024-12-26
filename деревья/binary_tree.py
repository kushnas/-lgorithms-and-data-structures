class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, key):
        self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:  
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    def _find_min_recursively(self, node):
        if node.left is None:
            return node.value
        return self._find_min_recursively(node.left)


    def _find_max_recursively(self, node):
        if node.right is None:
            return node.value
        return self._find_max_recursively(node.right)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None:
            return False
        
        if key == node.value:
            return True
        elif key < node.value:
            return self._search_recursively(node.left, key)
        else:
            return self._search_recursively(node.right, key)
        
    def delete(self, key):
            self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        if node is None:
            return node
        
        if key < node.value:
            node.left = self._delete_recursively(node.left, key)
        elif key > node.value:
            node.right = self._delete_recursively(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
           
            temp = self._find_min_recursively(node.right)
            node.value = temp
            node.right = self._delete_recursively(node.right, temp)
        
        return node
    
    def breadth_first_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            current_node = queue.pop(0)  
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result


    def depth_first_traversal(self):
        result = []
        self._depth_first_traversal_recursively(self.root, result)
        return result

    def _depth_first_traversal_recursively(self, node, result):
        if node:
            
            self._depth_first_traversal_recursively(node.left, result)
            result.append(node.value)
            self._depth_first_traversal_recursively(node.right, result)


import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        """ Метод, который вызывается перед каждым тестом. """
        self.tree = BinaryTree(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(13)
        self.tree.insert(17)

    def test_find_min(self):
        """ Тест метода поиска минимального значения """
        min_value = self.tree._find_min_recursively(self.tree.root)
        self.assertEqual(min_value, 3, "Minimum should be 3")

    def test_find_max(self):
        """ Тест метода поиска максимального значения """
        max_value = self.tree._find_max_recursively(self.tree.root)
        self.assertEqual(max_value, 17, "Maximum should be 17")

    def test_search(self):
        """ Тест метода поиска элемента в дереве """
        self.assertTrue(self.tree.search(7), "Should find 7 in the tree")
        self.assertTrue(self.tree.search(15), "Should find 15 in the tree")
        self.assertTrue(self.tree.search(3), "Should find 3 in the tree")
        self.assertFalse(self.tree.search(8), "Should not find 8 in the tree")
        self.assertFalse(self.tree.search(20), "Should not find 20 in the tree")

    def test_breadth_first_traversal(self):
        """ Тест обхода графа в ширину """
        bfs_result = self.tree.breadth_first_traversal()
        self.assertEqual(bfs_result, [10, 5, 15, 3, 7, 13, 17], "BFS traversal should match")

    def test_depth_first_traversal(self):
        """ Тест обхода графа в глубину """
        dfs_result = self.tree.depth_first_traversal()
        self.assertEqual(dfs_result, [3, 5, 7, 10, 13, 15, 17], "DFS traversal should match")

    def test_delete(self):
        """ Тест удаления элемента из дерева """
        self.tree.delete(15)
        self.assertFalse(self.tree.search(15), "Should not find 15 in the tree after deletion")

        self.tree.delete(10)  # Удаляем корень
        self.assertFalse(self.tree.search(10), "Should not find 10 in the tree after deletion of root")
        self.assertEqual(self.tree.depth_first_traversal(), [3, 5, 7, 13, 17], 
                         "DFS after deleting root should match")

if __name__ == "__main__":
    unittest.main()