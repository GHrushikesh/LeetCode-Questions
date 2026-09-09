# #3870 - 3870. Count Commas in Range

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `295` |
| **Memory** | `19232000` |
| **Topic Tags** | `Math` |
| **Date** | `2026-09-09 22:48` |

## Solution

```python3
class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0 
        for i in range(1000, n + 1):
            ans += 1
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*