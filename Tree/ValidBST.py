
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def validate(node, low=-float("inf"), high=float("inf")):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return (validate(node.left, low, node.val)) and (validate(node.right, node.val, high))

    return validate(root)
