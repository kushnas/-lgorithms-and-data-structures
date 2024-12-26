class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.balance_factor = 0


class AVLTree:
    def __init__(self):
        self.root = None


    def insert(self, key):
        node = Node(key)
        p = None
        cur = self. root

        while cur is not None:
            p = cur
            if node.data < cur.data:
                cur = cur.left
            else:
                cur = cur.right

        node.parent = p
        if p is None:

            self.root = node

        elif node.data < p.data:
            p.left = node
        else:
            p.right = node

        self.updateBalance(node)


    # проставляем balance_factor для узла
    def updateBalance(self, node):
        if node.balance_factor < -1 or node.balance_factor > 1:
            self.rebalance(node)
            return
        
        if node.parent is not None:
    # если вставляем левый узел  декрементируем баланс
            if node == node.parent.left:
                node.parent.balance_factor -= 1
    # если вставляем правый узел инкрементируем баланс
        if node == node.parent.right:
            node.parent.balance_factor += 1
        if node.parent.balance_factor != 0:
    # вызываем рекурсивно, чтобы понять # нужна ли нам балансировка дерева
            self.updateBalance(node.parent)

    def reBalance(self, node):
        print("До врацения")
        self.prettyPrint()
        if node.balance_factor > 0:
            if node.right.balance_factor <0:
                self.rightRotate(node.right)
                self.leftRotate(node)
            else:
                self.leftRotate(node)

        elif node.balance_factor <0:
            if node.left.balance_factor>0:
                self.leftRotate(node.left)
                self.rightRotate(node)
            else:
                self.rightRotate(node)
        print('После вращения')
        self.prettyPrint()


    def leftRotate(self, node):
        print('Левое вращение')
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent=node

        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right=right_child
        right_child.left=node
        node.parent = right_child

        node.balance_factor = node.balance_facror -1 - max(0, right_child.balance_factor)
        right_child.balance_factor = right_child.balance_factor -1 + min(0, node.balance_factor)



    
import unittest

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()

    def test_insert_single_node(self):
        self.tree.insert(10)
        self.assertEqual(self.tree.root.data, 10)
        self.assertIsNone(self.tree.root.parent)
        self.assertIsNone(self.tree.root.left)
        self.assertIsNone(self.tree.root.right)

    def test_insert_multiple_nodes(self):
        nodes = [10, 20, 30]
        for node in nodes:
            self.tree.insert(node)


        self.assertEqual(self.tree.root.data, 20)
        self.assertEqual(self.tree.root.left.data, 10)
        self.assertEqual(self.tree.root.right.data, 30)

    def test_balance_factor_after_insertion(self):
        nodes = [10, 20, 30]
        for node in nodes:
            self.tree.insert(node)


        self.assertEqual(self.tree.root.balance_factor, 0)
        self.assertEqual(self.tree.root.left.balance_factor, 0)
        self.assertEqual(self.tree.root.right.balance_factor, 0)

    def test_left_rotation(self):
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(10)  

        self.assertEqual(self.tree.root.data, 20)
        self.assertEqual(self.tree.root.left.data, 10)
        self.assertEqual(self.tree.root.right.data, 30)

    def test_right_rotation(self):
      
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)  

        self.assertEqual(self.tree.root.data, 20)
        self.assertEqual(self.tree.root.left.data, 10)
        self.assertEqual(self.tree.root.right.data, 30)

if __name__ == '__main__':
    unittest.main()