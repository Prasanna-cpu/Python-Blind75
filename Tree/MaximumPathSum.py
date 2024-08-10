class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root:TreeNode):
    max_sum=float("-inf")
    def maxHelper(node:TreeNode):
        nonlocal max_sum
        if not node:
            return 0
        left_sum=max(0,maxHelper(node.left))
        right_sum=max(0,maxHelper(node.right))

        curr_sum=node.val+left_sum+right_sum
        max_sum=max(max_sum,curr_sum)

        return node.val+max(left_sum+right_sum)
    maxHelper(root)
    return max_sum