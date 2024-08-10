class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder: [], postorder: []):
    if not inorder or not postorder:
        return None

    root_val = postorder.pop()

    root = TreeNode(root_val)

    root_idx = inorder.index(root_val)

    root.left = buildTree(inorder[:, root_idx], postorder)
    root.right = buildTree(inorder[root_idx + 1:], postorder)

    return root
