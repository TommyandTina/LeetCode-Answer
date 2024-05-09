# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right) ->bool:
            if not left and not right: return True
            if not left or not right: return False
            return (left.val == right.val) and dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)

#iterative solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack = [(root.left,root.right)]
        while stack:
            left,right = stack.pop()
            if not left and not right: continue
            if not left or not right or left.val != right.val: return False
            stack.append((left.left,right.right))
            stack.append((left.right,right.left))
        return True