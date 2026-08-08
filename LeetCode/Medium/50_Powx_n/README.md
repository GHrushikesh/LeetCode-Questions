# #50 - 50. Pow(x, n)

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19440000` |
| **Topic Tags** | `Math, Recursion` |
| **Date** | `2026-08-08 19:14` |

## Solution

```python3
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        ans = 1
        while n:
            if n % 2:
                ans *= x
            
            x *= x
            n //= 2
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*