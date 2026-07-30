# #997 - 997. Find the Town Judge

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `6` |
| **Memory** | `22652000` |
| **Topic Tags** | `Array, Hash Table, Graph Theory` |
| **Date** | `2026-07-30 21:46` |

## Solution

```python3
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)
        for a , b in trust:
            count[a] -= 1
            count[b] += 1
        for i in range(1, n+1):
            if count[i] == n - 1:
                return i
        return -1
```

---
*Generated automatically by [RG Sync](https://github.com).*