class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=0:
            return 0
        profit = 0
        i,j = 0,1
        while(j<len(prices)):
            if prices[i]<prices[j] and prices[j]-prices[i] > profit:
                profit  = max(profit,prices[j]-prices[i])
            if prices[i]>prices[j]:
                i+=1
            if prices[j]<prices[i]:
                i=j
            j+=1
        return profit
        