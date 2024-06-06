
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)
            elements.append(node.value)
            self._inorder_traversal(node.right, elements)
    
    def sum_of_tree(self):
        return self._sum_of_tree(self.root)
    
    def _sum_of_tree(self, node):
        if node is None:
            return 0
        return node.value + self._sum_of_tree(node.left) + self._sum_of_tree(node.right)

# Приклад використання
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    total_sum = bst.sum_of_tree()
    print("Сума всіх значень у дереві:", total_sum)
