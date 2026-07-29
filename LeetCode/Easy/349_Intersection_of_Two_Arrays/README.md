# #349 - 349. Intersection of Two Arrays

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Easy` |
| **Language** | `Python3` |
| **Runtime** | `N/A` |
| **Memory** | `19432000` |
| **Topic Tags** | `Array, Hash Table, Two Pointers, Binary Search, Sorting` |
| **Date** | `2026-07-24 19:28` |

## Solution

```python3
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for a in nums1:
            count[a] = 1
        result = []

        for a in nums2:
            if a in count:
                result.append(a)
                del count[a]
        return result
```

---
*Generated automatically by [RG Sync](https://github.com).*