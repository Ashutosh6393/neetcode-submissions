# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root: 
            return []



        x = self.preorderTraversal(root.left)
        m = [root.val]
        m = m + x
        y = self.preorderTraversal(root.right)

        return m + y

        