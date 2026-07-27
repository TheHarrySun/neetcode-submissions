# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        flat = []

        stack = [root]

        seen = set()

        while stack:
            node = stack[-1]

            if node.left and node.left not in seen:
                stack.append(node.left)
                continue
            stack.pop()
            flat.append(node.val)
            seen.add(node)
            if node.right and node.right not in seen:
                stack.append(node.right)
        print(flat)
        return flat[k - 1]