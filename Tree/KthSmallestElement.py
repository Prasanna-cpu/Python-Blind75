class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: TreeNode,k:int):
    def inorder(node: TreeNode):
        if not node:
            return []

        return inorder(node.left) + [node.val] + inorder(node.right)

    sorted_arr=inorder(root)
    return sorted_arr[k-1]


