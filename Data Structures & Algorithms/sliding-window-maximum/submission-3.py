class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        # right = k - 1

        res = []

        heap = []

        while left < len(nums):

            heapq.heappush_max(heap, [nums[left], left])

            if left >= k -1 :
                while heap[0][1] <= left -k:
                    heapq.heappop_max(heap)


        
                res.append(heap[0][0])
            left += 1
            
            
        return res
        


            

           




        