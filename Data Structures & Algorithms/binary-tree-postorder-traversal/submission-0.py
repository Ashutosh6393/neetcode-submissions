# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: 
            return []

        
        x = self.postorderTraversal(root.left)
        y = self.postorderTraversal(root.right)

        return x + y + [root.val]