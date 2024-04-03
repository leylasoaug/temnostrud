class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Example to insert a new node with value 4
root = insert(root, 4)
