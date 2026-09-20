class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            buy=prices[i]
            sell=prices[i]
            for j in range(i+1,len(prices)):
                if prices[j]>sell:
                    sell=prices[j]
            profit=max(profit,sell-buy)
        return profit
                
        