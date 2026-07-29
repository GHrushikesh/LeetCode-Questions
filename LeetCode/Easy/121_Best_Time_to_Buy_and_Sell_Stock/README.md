# #121 - 121. Best Time to Buy and Sell Stock

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `45` |
| **Memory** | `28616000` |
| **Topic Tags** | `Array, Dynamic Programming` |
| **Date** | `2026-06-05 15:48` |

## Solution

```python3
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
```

---
*Generated automatically by [RG Sync](https://github.com).*