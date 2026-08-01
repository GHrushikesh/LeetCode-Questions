# #33 - 33. Search in Rotated Sorted Array

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19572000` |
| **Topic Tags** | `Array, Binary Search` |
| **Date** | `2026-08-01 19:14` |

## Solution

```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums) - 1
        while st <= end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                return mid
            if nums[st] <= nums[mid]:
                if nums[st] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    st = mid + 1
                else:
                    end = mid - 1
        return -1
```

---
*Generated automatically by [RG Sync](https://github.com).*