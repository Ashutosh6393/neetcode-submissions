# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        
        hmap = {}

        for l in lists:
          
            ptr = l

            while ptr: 
                hmap[ptr.val] = hmap.get(ptr.val, 0) + 1
                ptr = ptr.next
                # i += 1
        
        hmap = dict(sorted(hmap.items()))

        dummy = ListNode()
        ptr = dummy

        for k,v in hmap.items():

            count = v
            while count>0: 
                node = ListNode(k)
                ptr.next = node
                ptr = ptr.next
                count -= 1
        
        return dummy.next



            

        


