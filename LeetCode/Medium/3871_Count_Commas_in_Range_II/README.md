# #3871 - 3871. Count Commas in Range II

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19156000` |
| **Topic Tags** | `Math` |
| **Date** | `2026-09-09 22:49` |

## Solution

```python3
class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        commas = 1
        while start <= n:
            end = start * 1000 - 1
            if n < end:
                count = n - start + 1
            else:
                count = end - start + 1
            ans += count * commas
            start = start * 1000
            commas += 1
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*