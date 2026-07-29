# #1512 - 1512. Number of Good Pairs

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19216000` |
| **Topic Tags** | `Array, Hash Table, Math, Counting` |
| **Date** | `2026-07-19 21:43` |

## Solution

```python3
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count
```

---
*Generated automatically by [RG Sync](https://github.com).*