# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower = float('-inf')
        upper = float('inf')
        def solve(root, lower, upper):
            if root is None:
                return True
            if not lower < root.val < upper:
                return False
            value = root.val
            return solve(root.left, lower, value) and solve(root.right, value, upper)
        return solve(root, lower, upper)