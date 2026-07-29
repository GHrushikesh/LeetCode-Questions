# #387 - 387. First Unique Character in a String

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `75` |
| **Memory** | `19564000` |
| **Topic Tags** | `Hash Table, String, Queue, Counting` |
| **Date** | `2026-07-20 18:18` |

## Solution

```python3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1 
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1
```

---
*Generated automatically by [RG Sync](https://github.com).*