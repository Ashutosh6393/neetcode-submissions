class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)


        largest = 0

        for n in nums:
            if (n - 1) not in count: 
                streak = 1
                current = n
                while count.get(current+1, False):
                    current += 1
                    streak += 1
                
                largest = max(streak, largest)

        return largest
