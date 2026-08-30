# #7 - 7. Reverse Integer

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `37` |
| **Memory** | `19076000` |
| **Topic Tags** | `Math` |
| **Date** | `2026-08-26 15:48` |

## Solution

```python3
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        ans = 0
        while x > 0:
            digit = x % 10
            ans = ans * 10 + digit
            x = x // 10
        ans = ans * sign
        if ans < -2147483648 or ans > 2147483647:
            return 0

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*