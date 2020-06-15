    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right,val)
