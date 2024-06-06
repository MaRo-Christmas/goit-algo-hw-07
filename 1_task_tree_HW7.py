
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_maximum(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Приклад використання:
root = TreeNode(10)
root = insert(root, 20)
root = insert(root, 5)
root = insert(root, 30)
root = insert(root, 15)

print("Найбільше значення в дереві:", find_maximum(root))
