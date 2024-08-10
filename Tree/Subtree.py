
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(self, root: TreeNode, subRoot:TreeNode) -> bool:
    def identical(tree1, tree2):
        if not tree1 and not tree2:
            return True

        if not tree1 or not tree2:
            return False

        return (tree1.val == tree2.val) and (identical(tree1.left, tree2.left)) and (
            identical(tree1.right, tree2.right))

    if not root:
        return False

    if identical(root, subRoot):
        return True

    return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))