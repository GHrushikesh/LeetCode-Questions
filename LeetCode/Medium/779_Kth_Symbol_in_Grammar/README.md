# #779 - 779. K-th Symbol in Grammar

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19348000` |
| **Topic Tags** | `Math, Bit Manipulation, Recursion` |
| **Date** | `2026-08-09 10:48` |

## Solution

```python3
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0 
        half = 2 ** (n - 2)

        if k <= half:
            return self.kthGrammar(n - 1, k)
        return 1 - self.kthGrammar(n-1,k-half)
```

---
*Generated automatically by [RG Sync](https://github.com).*