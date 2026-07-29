# #724 - 724. Find Pivot Index

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `5` |
| **Memory** | `20388000` |
| **Topic Tags** | `Array, Prefix Sum` |
| **Date** | `2026-07-26 19:26` |

## Solution

```python3
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range (len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
```

---
*Generated automatically by [RG Sync](https://github.com).*