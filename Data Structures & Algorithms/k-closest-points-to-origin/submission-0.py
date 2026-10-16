class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distances = []

        heap = []


        for x, y in points: 

            distance = math.sqrt((x)**2 + (y)**2)   
            
            heapq.heappush_max(heap, [distance, x, y])

            if len(heap) > k: 
                heapq.heappop_max(heap)
            
        
        res =[]
        while heap:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
        

        return res