# #217 - 217. Contains Duplicate

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `17` |
| **Memory** | `32284000` |
| **Topic Tags** | `Array, Hash Table, Sorting` |
| **Date** | `2026-07-16 18:31` |

## Solution

```python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

---
*Generated automatically by [RG Sync](https://github.com).*