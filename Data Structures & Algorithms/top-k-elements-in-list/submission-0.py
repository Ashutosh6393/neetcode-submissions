class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        di = {}

        for n in nums:
            if n in di: 
                di[n] = di[n] + 1
            else:
                di[n] = 1

        # we have to sort by the value of di

        
        res = []
        while k>0:
            x = 0
            dele = None
            for key, val in di.items():
                if val > x:
                    x = val
                    dele = key
                    

            res.append(dele)
            di.pop(dele)
            k -= 1

        return res
        




        
            