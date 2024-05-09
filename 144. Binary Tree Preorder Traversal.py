# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#iterative solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        result = []
        while cur or stack:
            if cur:
                result.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return result

#recursive solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Khởi tạo danh sách để lưu kết quả
        result = []
        
        # Hàm đệ quy để thực hiện preorder traversal
        def preorder(node):
            if not node:
                return
            # Thêm giá trị của node vào danh sách kết quả
            result.append(node.val)
            # Duyệt qua cây con trái của node
            preorder(node.left)
            # Duyệt qua cây con phải của node
            preorder(node.right)
        
        # Gọi hàm đệ quy để thực hiện preorder traversal từ root
        preorder(root)
        
        return result
