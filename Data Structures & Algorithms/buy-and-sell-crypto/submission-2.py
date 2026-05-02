class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        msp = 0
        maxProfit = 0
        _len = len(prices)
        for i in range(_len-2, -1, -1):
            msp = max(msp, prices[i+1])
            maxProfit = max(maxProfit, msp - prices[i])

        return maxProfit


        