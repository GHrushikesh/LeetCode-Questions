# #1 - 1. Two Sum

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `18892000` |
| **Topic Tags** | `Array, Hash Table` |
| **Date** | `2025-09-30 15:12` |

## Solution

```python3
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # maps value -> index
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
        # Problem guarantees a solution; raise for safety
        raise ValueError("No two sum solution")
```

---
*Generated automatically by [RG Sync](https://github.com).*