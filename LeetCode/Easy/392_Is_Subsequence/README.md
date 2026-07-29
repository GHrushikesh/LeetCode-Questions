# #392 - 392. Is Subsequence

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19216000` |
| **Topic Tags** | `Two Pointers, String, Dynamic Programming` |
| **Date** | `2026-07-29 22:22` |

## Solution

```python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for ch in t:
            if i < len(s) and s[i] == ch:
                i+=1
        return i == len(s)
```

---
*Generated automatically by [RG Sync](https://github.com).*