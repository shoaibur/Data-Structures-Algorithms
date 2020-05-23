class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = Node
# Create a tree
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)

# Traverse
# Pre-order
def pre_order(tree):
    out = []
    def traverse(tree):
        if tree:
            out.append(tree.value)
            traverse(tree.left)
            traverse(tree.right)
    traverse(tree)
    return out
  
# In-order
def pre_order(tree):
    out = []
    def traverse(tree):
        if tree:
            traverse(tree.left)
            out.append(tree.value)
            traverse(tree.right)
    traverse(tree)
    return out

# Post-order
def pre_order(tree):
    out = []
    def traverse(tree):
        if tree:
            traverse(tree.left)
            traverse(tree.right)
            out.append(tree.value)
    traverse(tree)
    return out
