# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        ptr = head

        hmap = {}
        index = -1

        counter = 0

        while ptr is not None:

            if hmap.get(ptr, None): 
                index = hmap.get(ptr)
                return True
            
            hmap[ptr] = counter
            counter += 1
            ptr = ptr.next

        return False
        


        