# #3550 - 3550. Smallest Index With Digit Sum Equal to Index

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19316000` |
| **Topic Tags** | `Array, Math` |
| **Date** | `2026-09-24 17:58` |

## Solution

```python3
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def get_digit_sum(num: int) -> int:
            total = 0
            while num:
                num, digit = divmod(num, 10)
                total += digit
            return total

        for i, num in enumerate(nums):
            if get_digit_sum(num) == i:
                return i

        return -1
```

---
*Generated automatically by [RG Sync](https://github.com).*