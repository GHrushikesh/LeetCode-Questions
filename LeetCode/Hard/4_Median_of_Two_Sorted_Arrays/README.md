# #4 - 4. Median of Two Sorted Arrays####

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Hard` |
| **Language** | `Python` |
| **Runtime** | `2` |
| **Memory** | `12488000` |
| **Topic Tags** | `Array, Binary Search, Divide and Conquer` |
| **Date** | `2026-05-21 11:03` |

## Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)

        if n % 2 == 1:
            return float(nums[n // 2])

        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0
```

---
*Generated automatically by [RG Sync](https://github.com).****
