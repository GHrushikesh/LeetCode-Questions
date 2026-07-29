class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0 
        minValuesoFar = prices[0]
        for i in range (1, len(prices)):
           profit = prices[i]  - minValuesoFar
           if profit > ans:
            ans = profit
           if(prices[i]<minValuesoFar):
            minValuesoFar = prices[i]
        return ans