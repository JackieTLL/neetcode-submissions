class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        runningMin = []
        for price in prices:
            if runningMin == []:
                runningMin.append(price)
            else:
                runningMin.append(min(runningMin[-1], price))
        profit = []
        for i in range(len(prices)):
            profit.append(prices[i] - runningMin[i])
        return max(profit)
            
        