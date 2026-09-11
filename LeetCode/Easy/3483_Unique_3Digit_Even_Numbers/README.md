# #3483 - 3483. Unique 3-Digit Even Numbers

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `15` |
| **Memory** | `19484000` |
| **Topic Tags** | `Array, Hash Table, Recursion, Enumeration` |
| **Date** | `2026-09-11 16:55` |

## Solution

```python3
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        vis = [False] * 1000
        ans = 0
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    x = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not vis[x]:
                        vis[x] = True
                        ans += 1
        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*