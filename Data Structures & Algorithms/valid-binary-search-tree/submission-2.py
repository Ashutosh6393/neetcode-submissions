# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))

       

    def valid(self, root: Optional[TreeNode], left_min: float, right_max: float)-> bool:

        if not root: 
            return True
        

        if not (left_min < root.val < right_max):
            return False
        
        return self.valid(root.left, left_min, root.val ) and self.valid(root.right, root.val, right_max )




        
        


        