# #485 - 485. Max Consecutive Ones

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python` |
| **Runtime** | `15` |
| **Memory** | `13540000` |
| **Topic Tags** | `Array` |
| **Date** | `2026-06-05 12:33` |

## Solution

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        current = 0
        best = 0

        for num in nums:

            if num == 1:
                current = current + 1

                if current > best:
                    best = current

            else:
                current = 0

        return best
```

---
*Generated automatically by [RG Sync](https://github.com).*