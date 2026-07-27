# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        root1 = p
        root2 = q
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()
            if not n1 and not n2:
                continue
            elif (n1 and not n2) or (not n1 and n2):
                return False
            if n1.val != n2.val:
                return False
            q1.append(n1.left)
            q1.append(n1.right)
            q2.append(n2.left)
            q2.append(n2.right)
        if (q1 and not q2) or (not q1 and q2):
            return False
        return True