# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def maxDepth(root):
            if root is None:
                return 0
            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)
            self.res = max(self.res, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        maxDepth(root)
        return self.res

        