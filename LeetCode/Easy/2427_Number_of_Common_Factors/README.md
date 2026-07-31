# #2427 - 2427. Number of Common Factors

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19316000` |
| **Topic Tags** | `Math, Enumeration, Number Theory` |
| **Date** | `2026-07-31 18:37` |

## Solution

```python3
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0  and b % i == 0:
                count += 1
        return count
```

---
*Generated automatically by [RG Sync](https://github.com).*