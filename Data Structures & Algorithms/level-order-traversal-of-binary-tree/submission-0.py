# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque()
        ar = [[]]
        queue.append(root)

        curr = 1
        nxt = 0

        
        while queue: 
            q = queue.popleft()

            if curr != 0: 
                ar[-1].append(q.val)
                curr -= 1
            else: 
                curr = nxt
                nxt = 0
                ar.append([q.val])
                curr -= 1
            
            if q.left and q.right: 
                nxt += 2
            elif q.left or q.right: 
                nxt += 1
            else: 
                nxt += 0

            if q.left: 
                queue.append(q.left)
            
            if q.right: 
                queue.append(q.right)
            
        return ar
