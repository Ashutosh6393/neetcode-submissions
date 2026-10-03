class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1: 
            return 0


        left = 0

        profit = 0
        
        for i in range(1, len(prices)):
            curr = prices[i] - prices[left]

            profit = max(profit, curr)

            if prices[i] < prices[left]:
                left = i

        
        return profit


        