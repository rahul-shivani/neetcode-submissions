class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _len = len(prices)
        _max = -1
        maxProfit = 0        
        for idx in range(_len-2, -1, -1):
            _max = max(_max, prices[idx+1])
            maxProfit = max(maxProfit, _max - prices[idx])        

        return maxProfit


        