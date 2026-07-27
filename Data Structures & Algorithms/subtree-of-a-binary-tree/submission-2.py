# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            node = q.popleft()

            if not node:
                continue
            if node.val == subRoot.val and self.checkIfSame(node, subRoot):
                return True
            q.append(node.left)
            q.append(node.right)
        return False
    
    def checkIfSame(self, p, q):
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                n1 = q1.popleft()
                n2 = q2.popleft()

                if not n1 and not n2:
                    continue
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
        return True