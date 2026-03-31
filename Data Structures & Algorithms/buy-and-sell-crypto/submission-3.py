class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_buy = 0
        best_bet = 0
        for high_sell in range(1,len(prices)):
            if prices[low_buy]<prices[high_sell]:
                best_bet = max(prices[high_sell]-prices[low_buy],best_bet)
            else:
                low_buy=high_sell
        return best_bet