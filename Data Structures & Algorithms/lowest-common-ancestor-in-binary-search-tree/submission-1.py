# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        mp = {None: (False, False)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                stack.pop()
                
                containsP = mp[node.left][0] or mp[node.right][0]
                containsQ = mp[node.left][1] or mp[node.right][1]

                if node.val == p.val:
                    containsP = True
                if node.val == q.val:
                    containsQ = True
                if containsP and containsQ:
                    return node
                mp[node] = (containsP, containsQ)
        return root