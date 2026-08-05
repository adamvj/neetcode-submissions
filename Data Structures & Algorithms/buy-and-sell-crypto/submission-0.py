class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#        highindx = 0
#        lowindx = 0
        profitmax = 0
        for i in range(0, len(prices), 1):
            j = len(prices)-1
            while j > i:
                if prices[j] - prices[i] > profitmax:
                    profitmax = prices[j] - prices[i]
                j -=1
        return profitmax
                    
                