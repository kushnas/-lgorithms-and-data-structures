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


def find_height(root):
    if not root:
        return -1

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    return max(left_height, right_height) + 1


def inorder(root, row, col, height, ans):
    if not root:
        return

    offset = 2 ** (height - row - 1)

    if root.left:
        inorder(root.left, row + 1, col - offset, height, ans)

    ans[row][col] = str(root.value)

    if root.right:
        inorder(root.right, row + 1, col + offset, height, ans)

def tree_to_matrix(root):
    height = find_height(root)


    rows = height + 1
    cols = 2 ** (height + 1) - 1

    ans = [["" for _ in range(cols)] for _ in range(rows)]

    inorder(root, 0, (cols - 1) // 2, height, ans)

    return ans

def print_2d_array(arr):
    for row in arr:
        for cell in row:
            if cell == "":
                print(" ", end="")
            else:
                print(cell, end="")
        print()

def array_to_tree_visualization(array):
    """Преобразует массив в бинарное дерево и визуализирует его."""
    root = build_tree_from_array(array)
    result = tree_to_matrix(root)
    print_2d_array(result)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    array_to_tree_visualization(array)