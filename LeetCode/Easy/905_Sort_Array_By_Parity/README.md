# #905 - 905. Sort Array By Parity

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `2` |
| **Memory** | `19744000` |
| **Topic Tags** | `Array, Two Pointers, Sorting` |
| **Date** | `2026-07-29 17:57` |

## Solution

```python3
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0:
                left += 1

            if nums[right] % 2 == 1:
                right -= 1

        return nums
```

---
*Generated automatically by [RG Sync](https://github.com).*