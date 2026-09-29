# #509 - 509. Fibonacci Number

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `377` |
| **Memory** | `19340000` |
| **Topic Tags** | `Math, Dynamic Programming, Recursion, Memoization` |
| **Date** | `2026-09-29 21:33` |

## Solution

```python3
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        first = self.fib(n - 1)
        second = self.fib(n - 2)
        answer = first + second
        return answer
```

---
*Generated automatically by [RG Sync](https://github.com).*