class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 9999
        maxProfit = 0

        for i in range(0, len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, prices[i])
        
        return maxProfit
        


        