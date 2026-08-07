# #70 - 70. Climbing Stairs

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19276000` |
| **Topic Tags** | `Math, Dynamic Programming, Memoization` |
| **Date** | `2026-08-07 19:08` |

## Solution

```python3
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

---
*Generated automatically by [RG Sync](https://github.com).*