# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter = 0
    
        def height(node):
            nonlocal diameter
            if not node:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            diameter = max(diameter, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        height(root)
        return diameter