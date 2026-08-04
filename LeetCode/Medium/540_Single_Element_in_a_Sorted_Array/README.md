# #540 - 540. Single Element in a Sorted Array

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `26964000` |
| **Topic Tags** | `Array, Binary Search` |
| **Date** | `2026-08-04 21:52` |

## Solution

```python3
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left , right = 0 , len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2

            else:
                right = mid
                
        return nums[left]
```

---
*Generated automatically by [RG Sync](https://github.com).*