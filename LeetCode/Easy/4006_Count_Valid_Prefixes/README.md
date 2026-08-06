# #4006 - 4006. Count Valid Prefixes

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19280000` |
| **Topic Tags** | `None` |
| **Date** | `2026-08-01 20:05` |

## Solution

```python3
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ans = 0
        zero = 0
        one = 0
        for c in s:
            if c == '0':
                zero += 1
            else:
                one += 1
            if abs(zero - one) <= 1:
                ans += 1
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*