# #414 - 414. Third Maximum Number

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `3` |
| **Memory** | `19720000` |
| **Topic Tags** | `Array, Sorting` |
| **Date** | `2026-07-27 18:15` |

## Solution

```python3
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None

        for num in nums:

            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num

    
            elif second is None or num > second:
                third = second
                second = num

    
            elif third is None or num > third:
                third = num

        if third is None:
            return first

        return third
```

---
*Generated automatically by [RG Sync](https://github.com).*