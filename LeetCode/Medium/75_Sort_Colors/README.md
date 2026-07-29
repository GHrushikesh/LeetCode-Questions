# #75 - 75. Sort Colors

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19200000` |
| **Topic Tags** | `Array, Two Pointers, Sorting` |
| **Date** | `2026-06-09 23:58` |

## Solution

```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = len(nums) - 1
        i=0
        while i<= right:
            if (nums[i] == 0):
                nums[i] , nums[left] = nums[left] , nums [i]
                left += 1 
                i += 1 
            elif (nums[i] == 2):
                nums[i] , nums[right] = nums[right] , nums[i]
                right -= 1
            else:
                i += 1
```

---
*Generated automatically by [RG Sync](https://github.com).*