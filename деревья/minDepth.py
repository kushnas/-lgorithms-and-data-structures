from collections import deque
import unittest

##  через BFS

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def min_depth(root):
    """Находит минимальную глубину бинарного дерева."""
    if not root:
        return 0

    queue = deque([(root, 1)])  # Дек, который хранит кортежи (узел, глубина)
    
    while queue:
        node, depth = queue.popleft()
        
        # Проверяем, является ли текущий узел листом
        if not node.left or not node.right:
            return depth  # Возвращаем глубину, когда находим первый пустой лист

        # Добавляем дочерние узлы, если они существуют
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0

class TestMinDepth(unittest.TestCase):

    def test_empty_tree(self):
        # Пустое дерево имеет глубину 0
        root = None
        self.assertEqual(min_depth(root), 0)

    def test_single_node_tree(self):
        # Дерево с одним узлом имеет глубину 1
        root = TreeNode(1)
        self.assertEqual(min_depth(root), 1)

    def test_tree_with_only_left_nodes(self):
        # Дерево в виде цепочки по левым узлам
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(min_depth(root), 1)  

    def test_tree_with_only_right_nodes(self):
        # Дерево в виде цепочки по правым узлам
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(min_depth(root), 1)  

    def test_balanced_tree(self):
        # Пример сбалансированного дерева
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(min_depth(root), 2) 

    def test_tree_with_leaf_on_left(self):
        # Дерево с ближайшим листом на левой стороне
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(min_depth(root), 2) 


if __name__ == "__main__":
    unittest.main()