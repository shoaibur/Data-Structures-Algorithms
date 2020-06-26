def lowestCommonAncestor(root, p, q):
    if root is None: return root
    if p == root or q == root: return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if left is None and right is None: return None
    if left is not None and right is not None: return root
    
    return (left if left is not None else right)
