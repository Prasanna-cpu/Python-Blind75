class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def isSameTree(p:TreeNode,q:TreeNode):
    if not p and not q:
        return True

    if not p or not q:
        return False


    return (p.val == q.val) and (isSameTree(p.left,q.left)) and (isSameTree(p.right,q.right))


