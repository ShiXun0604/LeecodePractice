class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            profit = max(profit, prices[i] - min_price)
        
        return profit



prices = [7,1,5,3,6,4]
solution = Solution()
ans = solution.maxProfit(prices)
print(ans) 