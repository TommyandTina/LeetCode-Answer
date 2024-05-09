# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Khởi tạo danh sách để lưu kết quả
        result = []
        
        # Hàm đệ quy để thực hiện inorder traversal
        def inorder(node):
            if not node:
                return
            # Duyệt qua cây con trái của node
            inorder(node.left)
            # Thêm giá trị của node vào danh sách kết quả
            result.append(node.val)
            # Duyệt qua cây con phải của node
            inorder(node.right)
        
        # Gọi hàm đệ quy để thực hiện inorder traversal từ root
        inorder(root)
        return result

#iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Duyệt hết tất cả các nút bên trái của cây
            while current:
                stack.append(current)
                current = current.left
            
            # Lấy nút trên cùng của stack và thêm giá trị của nút vào danh sách kết quả
            current = stack.pop()
            result.append(current.val)
            
            # Duyệt qua cây con phải của nút
            current = current.right
        
        return result
