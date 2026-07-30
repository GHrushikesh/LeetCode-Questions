# #219 - 219. Contains Duplicate II

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `42` |
| **Memory** | `39416000` |
| **Topic Tags** | `Array, Hash Table, Sliding Window` |
| **Date** | `2026-07-30 18:48` |

## Solution

```python3
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for i in range(len(nums)):
            if nums[i] in last_index:
                if i - last_index[nums[i]] <= k:
                    return True
            last_index[nums[i]] = i
        return False
```

---
*Generated automatically by [RG Sync](https://github.com).*