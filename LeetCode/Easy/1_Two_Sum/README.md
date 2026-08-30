# #1 - 1. Two Sum

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `1481` |
| **Memory** | `19708000` |
| **Topic Tags** | `Array, Hash Table` |
| **Date** | `2026-08-30 22:58` |

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