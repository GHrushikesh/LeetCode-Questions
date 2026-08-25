# #35 - 35. Search Insert Position

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19944000` |
| **Topic Tags** | `Array, Binary Search` |
| **Date** | `2026-07-31 18:49` |

## Solution

```python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
```

---
*Generated automatically by [RG Sync](https://github.com).*