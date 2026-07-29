# #412 - 412. Fizz Buzz

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python` |
| **Runtime** | `N/A` |
| **Memory** | `13256000` |
| **Topic Tags** | `Math, String, Simulation` |
| **Date** | `2026-05-21 11:29` |

## Solution

```python
class Solution(object):
    def fizzBuzz(self, n):
        ans = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans
```

---
*Generated automatically by [RG Sync](https://github.com).*