# #1 - 1. Two Sum##

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `1737` |
| **Memory** | `19928000` |
| **Topic Tags** | `Array, Hash Table` |
| **Date** | `2026-07-28 11:44` |

## Solution

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,(len(nums))):
                if nums[i] + nums[j] == target:
                    return i,j
```

---
*Generated automatically by [RG Sync](https://github.com).*
