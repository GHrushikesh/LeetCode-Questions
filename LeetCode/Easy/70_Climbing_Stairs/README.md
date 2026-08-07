# #70 - 70. Climbing Stairs

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19276000` |
| **Topic Tags** | `Math, Dynamic Programming, Memoization` |
| **Date** | `2026-08-07 19:04` |

## Solution

```python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
        return second
```

---
*Generated automatically by [RG Sync](https://github.com).*