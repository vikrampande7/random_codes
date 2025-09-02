class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def inorder_traversal(root): # Left -> Root -> Right
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

def preorder_traversal(root): # Root -> Left -> Right
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root): # Left -> Right -> Root
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)


tree = Node(9)
tree.left = Node(4)
tree.right = Node(12)
tree.left.left = Node(2)
tree.left.right = Node(3)
tree.right.left = Node(10)
tree.right.right = Node(15)

# print(inorder_traversal(tree))
# print(preorder_traversal(tree))
print(postorder_traversal(tree))