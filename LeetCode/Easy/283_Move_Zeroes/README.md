# #283 - 283. Move Zeroes

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `7` |
| **Memory** | `20572000` |
| **Topic Tags** | `Array, Two Pointers` |
| **Date** | `2026-06-09 23:34` |

## Solution

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start =0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[i] , nums[start] = nums[start] , nums[i]
                start = start + 1
```

---
*Generated automatically by [RG Sync](https://github.com).*