# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        arr = []

        ptr = head
        while ptr:
            arr.append(ptr)
            ptr = ptr.next
        

        element_to_remove = len(arr) - n


        # if n == 1 and len(arr) == 1:
        #     return None
        


        if n == len(arr): 
            head = arr[element_to_remove].next
        elif n == 1 and len(arr) > 1:
            arr[element_to_remove-1].next = None
        else: 
            arr[element_to_remove-1].next = arr[element_to_remove+1]

        return head



