def serialize(self, root, data=[]):
    """Encodes a tree to a single string.
    """
    if root is None:
        data.append(None)
    else:
        data.append(root.val)
        self.serialize(root.left, data)
        self.serialize(root.right, data)
    return data

def deserialize(self, data):
    """Decodes your encoded data to tree.
    """
    if data[0] is None:
        data.pop(0)
        return
    root = TreeNode(data[0])
    data.pop(0)
    root.left = self.deserialize(data)
    root.right = self.deserialize(data)
    return root
