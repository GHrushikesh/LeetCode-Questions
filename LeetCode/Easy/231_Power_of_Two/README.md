# #231 - 231. Power of Two

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19260000` |
| **Topic Tags** | `Math, Bit Manipulation, Recursion` |
| **Date** | `2026-08-11 21:36` |

## Solution

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 ==0:
            n //= 2
        return n == 1
```

---
*Generated automatically by [RG Sync](https://github.com).*