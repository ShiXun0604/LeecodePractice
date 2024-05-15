class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # edge case
        if len(prices) <= 1:
            return 0
                
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        
        return profit


prices = [7,1,5,3,6,4]
solution = Solution()
ans = solution.maxProfit(prices)
print(ans) 