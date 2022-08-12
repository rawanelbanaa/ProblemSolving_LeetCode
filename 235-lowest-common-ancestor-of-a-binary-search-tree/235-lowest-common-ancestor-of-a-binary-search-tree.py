# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            pval, qval = p.val, q.val
            while root:
                val = root.val
                if val > max(pval, qval):
                    root = root.left
                elif val < min(pval, qval):
                    root = root.right
                else:
                    return root