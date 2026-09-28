# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, currMax):
            if root is None:
                return 0
            if root.val >= currMax:
                currMax = root.val
                return 1 + solve(root.left, currMax) + solve(root.right, currMax)
            else:
                return solve(root.left, currMax) + solve(root.right, currMax)
        return solve(root, float('-inf'))
        