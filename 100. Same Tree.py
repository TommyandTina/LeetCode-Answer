# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result_p = []
        result_q = []
        def preorder(node,result:List[int]):
            if not node:
                result.append(None)
                return
            # Thêm giá trị của node vào danh sách kết quả
            result.append(node.val)
            # Duyệt qua cây con trái của node
            preorder(node.left,result)
            # Duyệt qua cây con phải của node
            preorder(node.right,result)
        preorder(p,result_p)
        preorder(q,result_q)
        if result_p == result_q:
            return True
        else:
            return False

#another solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)