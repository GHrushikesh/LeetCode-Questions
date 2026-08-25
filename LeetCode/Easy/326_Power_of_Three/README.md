# #326 - 326. Power of Three

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `7` |
| **Memory** | `19400000` |
| **Topic Tags** | `Math, Recursion` |
| **Date** | `2026-08-10 20:52` |

## Solution

```python3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
```

---
*Generated automatically by [RG Sync](https://github.com).*