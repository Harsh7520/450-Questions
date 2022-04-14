class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        point = prices[0]
        for i in range(len(prices)):
            if(prices[i]<=point):
                point = prices[i]
            else:
                max_profit = max(max_profit,prices[i]-point)
        return(max_profit)
