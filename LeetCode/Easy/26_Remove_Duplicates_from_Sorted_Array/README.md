# #26 - 26. Remove Duplicates from Sorted Array

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `20492000` |
| **Topic Tags** | `Array, Two Pointers` |
| **Date** | `2026-07-28 18:50` |

## Solution

```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i + 1
```

---
*Generated automatically by [RG Sync](https://github.com).*